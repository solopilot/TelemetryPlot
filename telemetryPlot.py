'''
Created on Nov 26, 2016

@author: solo

Displays recorded log data for multiple variables in a tabular file (XLS, CSV or TSV)
Data for each variable should be in a column, the first row contains the variable's name
Booleans are converted to 1.0 or 0.0
xlrd does not distinguish between float and ints
also, pyqtgraph displays arrays of floats, so everything is in float
'''
from PyQt4 import QtGui, QtCore
#import pyqtgraph as pg
import sys
import webbrowser               # to display help files
from ui import uiPlotView       # ui screen built by QT Designer
import version                  # contains compile & build date

# globals
variables = []      # list of Variables, all recorded data is read in here
timer = None        # the first column, a varaiable with a list of time values
mainWindow = None
ui = None
widget = None       # pyqtgraph item
colors = [(255, 0, 0), (255, 153, 51), (255, 204, 153), (255, 255, 153), (204, 255, 153), (0, 255, 0), 
          (204, 255, 229), (0, 128, 255), (178, 102, 255)]
availColors = None  # available colors, copy of colors[]

# Variable represents one column in the recorded data
class Variable:
    def __init__(self, name, column):
        self.name = name        # name from header line
        self.column = column    # column index
        self.numeric = False    # plottable
        self.values = []        # list of recorded values for this variable
        self.displayValues = [] # nonnumeric values are converted to integers
        self.max = ''           # max value: empty
        self.min = ''
        self.list = []          # list of unique values for non numeric variables
        self.inactive = True    # is the value changing or not
        self.selected = False   # true if checkbox is checked
        self.color = None       # color of row & plot. value from availColors[], when selected
        self.items = []         # list of display items associated with variable's name

    # input param 'value' is a string; add it to list of values[]
    def addValue(self, value):
        try:                    # check if this is an int or float value
            value = float(value)
        except:
            pass                # leave it as a string
        self.values.append(value)

    # set min, max, numeric, inactive
    def analyze(self):
        try:
            sum(self.values)    # sum will crash if not numeric
            self.numeric = True
            self.displayValues = self.values    # same as values
            self.max = max(self.values)
            self.min = min(self.values)
            self.inactive = self.max == self.min    # non changing
        except:
            self.numeric = False
            # convert string values into list indices
            for val in self.values:
                if val not in self.list:
                    self.list.append(val)           # list of unique values, in order of appearance
                self.displayValues.append(self.list.index(val))
            self.inactive = len(self.list) <= 1     # non changing

# parse CSV data that was previously read in and set up globals variables[] and timer
# data must be lines separated by '\n'
# each line must be comma separated variables
def parseFile(data):
    global variables, timer, availColors
    variables = []          # reset global values
    timer = None
    availColors = colors[:] # make a copy of the list

    numLines = 0
    lines = data.split('\n')
    for line in lines:
        fields = line.strip().split(',')
        if len(fields) > 1  and  not fields[0].startswith('#'):
            if numLines == 0:       # first line is the header
                # pick up variable names in header line
                for col, name in enumerate(fields):     # fields is list of variable names
                    if name == '':                      # blank?
                        name = 'variable %s' % col
                    variable = Variable(name, col)
                    variables.append(variable)
            else:
                for col, value in enumerate(fields):    # fields is list of variable values
                    if col < len(variables):            # sometimes data has trailing garbage tabs
                        variable = variables[col]
                        variable.addValue(value)
            numLines += 1
        if numLines % 1000 == 0:
            displayStatus('%s of %s lines read' % (numLines, len(lines)))

    # compute variable properties
    for variable in variables:
        variable.analyze()

    if len(variables) > 0:
        timer = variables.pop(0)    # sets the timer column variable
        numLines -= 1
    return numLines

# convert Excel file to CSV
# booleans get converted to 1 & 0
# xlrd cannot distinguish between ints and floats
# returns CSV string , or None on error
def parseXLStoCSV(fileName):
    import xlrd
    try:
        workbook = xlrd.open_workbook(fileName)
        worksheet = workbook.sheet_by_index(0)
        data = ''
        for row in range(worksheet.nrows):
            values = []
            for col in range(worksheet.ncols):
                value = worksheet.cell(row, col).value
                cellType = worksheet.cell(row, col).ctype
                if cellType == xlrd.XL_CELL_NUMBER:
                    value = float(value)    # convert from str to float
                try:
                    value = str(value)      # Text, Boolean, None, ...
                except:
                    value = value.encode('ascii', 'ignore')
                if ',' in value:
                    value = '"%s"' % value
                values.append(value)
            data += ','.join(values)+'\n'
        return data
    except:         # this was not an XLS file
        displayStatus('Not an XLS file')
        return None

# fill the specified table with variable names
# there are 2 tables: selected and unselected
def displayVariables(table, selected, hideInactive):
    # need to set the row count BEFORE filling the table
    count = sum(1 for variable in variables if variable.selected == selected  and
                                                (not hideInactive or not variable.inactive))
    table.setRowCount(count)
    table.setSortingEnabled(False)
    n = 0
    for variable in variables:
        if variable.selected == selected  and    \
                (not hideInactive or not variable.inactive):
            item = QtGui.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Checked if variable.selected else QtCore.Qt.Unchecked)
            item.setText(variable.name)
            if variable.inactive:
                item.setTextColor(QtGui.QColor('red'))
            if variable.color != None:
                item.setBackgroundColor(QtGui.QColor(*variable.color))
            variable.items = [ item ]
            table.setItem(n, 0, item)

            item = QtGui.QTableWidgetItem()
            if variable.numeric:
                props = 'Min:%s, Max=%s' % (variable.min, variable.max)
            else:
                props = 'Text with %s values' % len(variable.list)
            item.setText(props)
            if variable.color != None:
                item.setBackgroundColor(QtGui.QColor(*variable.color))
            variable.items.append(item)
            table.setItem(n, 1, item)
            n += 1
    table.clearSelection()          # restore color from blue (selected)
    table.setSortingEnabled(True)
    table.resizeColumnsToContents()

# a checkbox or variable name was clicked in a table 
def itemClicked(item):
    for variable in variables:      # find item that was clicked
        if item in variable.items:  # non numeric variables not displayed
            break
    else:
        displayStatus('Please click on a variable')
        return
    if variable.selected:
        variable.selected = False
        availColors.append(variable.color)      # return color to end of list of available availColors
        variable.color = None
    else:
        if len(availColors) <= 0:
            displayStatus('You are viewing too many variables.  Kindly restrain yourself :-)')
            return
        variable.selected = True
        variable.color = availColors.pop()      # get last color
    displayAll()		# update both tables and plot

# "Hide Inactive" checkbox was clicked
def checkedStateChanged(item=None):
    hideInactive = ui.checkBoxHideInactive.isChecked()
    displayVariables(table=ui.varUnselectedTable, selected=False, hideInactive=hideInactive)

# plot all selected variables
def displayPlot():
    widget.clear()      # erase previous plots
    if timer != None:   # timer will be none if no file data is available, typically when bad file opened
        for variable in variables:
            if variable.selected:
                widget.plot(timer.values, variable.displayValues, name=variable.name, pen=variable.color)

# displays plot and variable tables
def displayAll():
    displayPlot()
    displayVariables(table=ui.varSelectedTable, selected=True, hideInactive=False)
    # could call checkedStateChanged()
    hideInactive = ui.checkBoxHideInactive.isChecked()
    displayVariables(table=ui.varUnselectedTable, selected=False, hideInactive=hideInactive)

# display line in status bar at bottom of screen
def displayStatus(msg):
    mainWindow.statusBar().showMessage(msg)

# connect display items with callback functions
def connectAll():
    ui.varSelectedTable.itemClicked.connect(itemClicked)
    ui.varUnselectedTable.itemClicked.connect(itemClicked)
    ui.checkBoxHideInactive.stateChanged.connect(checkedStateChanged)
    QtCore.QObject.connect(ui.buttonReset, QtCore.SIGNAL('clicked()'), buttonReset)
    QtCore.QObject.connect(ui.buttonCompressY, QtCore.SIGNAL('clicked()'), buttonCompressY)
    QtCore.QObject.connect(ui.actionExit, QtCore.SIGNAL('triggered()'), sysExit)
    QtCore.QObject.connect(ui.actionOpen_File, QtCore.SIGNAL('triggered()'), openFile)
    QtCore.QObject.connect(ui.actionAbout, QtCore.SIGNAL('triggered()'), about)
    QtCore.QObject.connect(ui.actionGeneral_Help, QtCore.SIGNAL('triggered()'), generalHelp)
    QtCore.QObject.connect(ui.actionHelp_with_Plots, QtCore.SIGNAL('triggered()'), helpWithPlots)
    #widget.plotItem.vb.sigResized.connect(updateViews)

# returns CSV data
def readFile(filename):
    parts = filename.lower().rsplit('.', 1) # convert .XLS to .xls
    extension = parts[-1]
    data = None
    if extension in ['xls', 'xlsx']:
        data = parseXLStoCSV(filename)  # convert XLS to CSV
    if data == None:                    # must be CSV/TSV file
        with open(filename, 'r') as f:
            data = f.read().replace('\t', ',')  # replace any tabs with commas
    return data

# prompt user for filename
def getFileName():
    fileExts = '*.csv *.tsv *.xls *.xlsx'
    filename = QtGui.QFileDialog.getOpenFileName(None, 'TelemetryPlot: Open log file', '', 'Files (%s)' % fileExts)
    if filename in [None, '']:      # cancelled
        return None
    return str(filename)            # convert qstring to str

# menu pick item
def openFile():
    filename = getFileName()                # prompt user for filename
    if filename != None:                    # cancelled?
        data = readFile(filename)           # returns CSV file
        numLines = parseFile(data)          # parse data into Variables
        displayStatus('File: %s, %s lines' % (filename, numLines))
        displayAll()

# menu pick item
def about():
    displayStatus('TelemetryPlot: Version %s  Cue Group' % version.versionDate)

# menu pick item
def generalHelp():
    webbrowser.open('generalHelp.html', new=0, autoraise=True)

# menu pick item
def helpWithPlots():
    webbrowser.open('helpWithPlots.html', new=0, autoraise=True)

# menu pick item
def sysExit():
    sys.exit()

# button for compress Y axis
def buttonCompressY():
    return  # disabled, causes divide by 0 exceptions
    if ui.buttonCompressY.text() == 'Compress Y Axis':
        widget.setLogMode(False, True)
        ui.buttonCompressY.setText('Restore Y Axis')
    else:   # Restore Y Axis
        widget.setLogMode(False, False)
        ui.buttonCompressY.setText('Compress Y Axis')

# button for Reset Plot
def buttonReset():
    widget.autoRange()
    widget.setLogMode(False, False)

def main():
    global mainWindow, ui, widget
    app = QtGui.QApplication(sys.argv)
    mainWindow =  QtGui.QMainWindow()
    ui = uiPlotView.Ui_MainWindow()
    ui.setupUi(mainWindow)

    ag = app.desktop().availableGeometry(-1)
    mainWindow.resize(ag.width()-10, ag.height()-40)   # magic val for windows app bar

    # to create ui.plotWidget, see
    #        http://www.pyqtgraph.org/documentation/how_to_use.html#embedding-widgets-inside-pyqt-applications
    # In Designer, create a QGraphicsView widget ("Graphics View" under the "Display Widgets" category).
    # Right-click on the QGraphicsView and select "Promote To...".
    # Under "Promoted class name", enter the class name you wish to use ("PlotWidget", "GraphicsLayoutWidget", etc).
    # Under "Header file", enter "pyqtgraph".
    # Click "Add", then click "Promote".
    widget = ui.plotWidget
    widget.showGrid(x=True, y=True, alpha=0.75)
    widget.setLabel('bottom', 'Time', 'Sec')
    widget.setLabels(left='Numeric Y Value')
    connectAll()

    if len(sys.argv) > 1:
        filename = sys.argv[1]          # command line param
    else:
        filename = getFileName()
        if filename == None:            # cancelled
            sysExit()

    data = readFile(filename)
    numLines = parseFile(data)
    displayStatus('File: %s, %s lines' % (filename, numLines))
    displayAll()

    mainWindow.show()
    sys.exit(app.exec_())

#####################
if __name__ == "__main__":
    main()