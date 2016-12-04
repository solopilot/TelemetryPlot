'''
Created on Nov 26, 2016

@author: solo

Displays recorded log data for multiple variables in a tabular file (XLS, CSV or TSV)
Data for each variable should be in a column, the first row contains the variable's name
xlrd converts booleans to 1 & 0; it does not distinguish between float and ints
'''
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
import sys
import webbrowser               # to display help files
from ui import uiPlotView       # ui screen built by QT Designer
import version                  # contains compile & build date

# globals
variables = None    # list of Variables, all recorded data is read in here
timer = None        # the first column, a variable with a list of time values
mainWindow = None	# Qt GUI stuff
ui = None
plotItem = None     # pyqtgraph PlotItem item
availColors = None  # available colors for plots, start with copy of colors[]

#constant
colors = [(255, 0, 0), (255, 153, 51), (255, 204, 153), (255, 255, 153), (204, 255, 153), (0, 255, 0), 
          (204, 255, 229), (0, 128, 255), (178, 102, 255)]

# Variable represents one column in the recorded data, one plot
class Variable:
    def __init__(self, name, column):
        self.name = name        # name from header line
        self.column = column    # column index in input table
        self.numeric = False    # plottable as values as opposed to strings
        self.values = []        # list of recorded values for this variable
        self.displayValues = [] # nonnumeric values are converted to integers
        self.max = ''           # max value: empty
        self.min = ''
        self.list = []          # list of unique values for non numeric variables
        self.inactive = True    # is the value changing or not
        self.selected = False   # true if variable is selected for display
        self.color = None       # color of variable & plot. value from availColors[], when selected
        self.axis = None        # axis item in plot, needed for tickStrings()
        self.vb = None          # viewBox item, needed for updateViews() on resize
        self.items = []         # list of row display items associated with variable in variable table

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
        except:     # went bang
            self.numeric = False
            # convert string values into list indices
            for val in self.values:
                if val not in self.list:
                    self.list.append(val)           # list of unique values, in order of appearance
                self.displayValues.append(self.list.index(val))
            self.inactive = len(self.list) <= 1     # non changing

            # check for boolean values
            if len(self.list) == 2:
                for v in self.list:
                    if v.lower() not in ['false', 'true']:
                        break       # not boolean
                else:           # yes boolean
                    # check if false comes before true
                    if self.list[0].lower() != 'false':
                        for i in range(self.displayValues): # flip the values
                            self.displayValues[i] = 1 - self.displayValues
                    self.list = ['False', 'True']   # need false to be 0 and true to be 1

# subclass AxisItem to provide text units
class TextAxisItem(pg.AxisItem):
    # overload tickStrings() to return values for this plot
    def tickStrings(self, values, scale, spacing):
        print 'tickStrings', self, values, scale, spacing
        for variable in variables:      # find variable associated with this axis item
            if self == variable.axis:
                break
        else:                           # this should not happen
            return [''] * len(values)   # return empty ticks

        ret = []
        for v in values:
            i = int(v)      # v can be a float
            s = variable.list[i] if i in range(len(variable.list)) else ''  # else empty str
            ret.append(s)
        return ret

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
        if numLines % 1000 == 0:                        # updates for the impatient
            displayStatus('%s of %s lines read' % (numLines, len(lines)))

    # compute variable properties
    for variable in variables:
        variable.analyze()

    if len(variables) > 0:
        timer = variables.pop(0)    # sets the timer column variable
        numLines -= 1

    return numLines

# prompt user for filename
def getFileName():
    fileExts = '*.csv *.tsv *.xls *.xlsx'
    filename = QtGui.QFileDialog.getOpenFileName(None, 'TelemetryPlot: Open log file', '', 'Files (%s)' % fileExts)
    if filename in [None, '']:      # cancelled
        return ''
    return str(filename)            # convert qstring to str

# returns CSV data
def readFile(filename):
    parts = filename.lower().rsplit('.', 1) # convert .XLS to .xls
    extension = parts[-1]
    data = ''
    if extension in ['xls', 'xlsx']:
        data = parseXLStoCSV(filename)  # convert XLS to CSV
    if data == '':                      # must be CSV/TSV file
        try:
            with open(filename, 'r') as f:
                data = f.read().replace('\t', ',')  # replace any tabs with commas
        except:
            pass        # return ''
    return data

# convert Excel file to CSV
# booleans get converted to 1 & 0
# xlrd cannot distinguish between ints and floats
# returns CSV string, or '' on error
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
        displayStatus('%s: Not an Excel file' % fileName)
        return ''

# fill the specified table with variable names
# there are 2 tables: selected and unselected
def displayVariables(table, selected, hideInactive):
    # need to set the row count BEFORE filling the table
    count = sum(1 for variable in variables if variable.selected == selected  and
                                                (not hideInactive or not variable.inactive))
    table.setRowCount(count)
    table.setSortingEnabled(False)
    nRow = 0
    for variable in variables:
        if variable.selected == selected  and    \
                (not hideInactive or not variable.inactive):
            item = QtGui.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Checked if variable.selected else QtCore.Qt.Unchecked)
            item.setText(variable.name)
            if variable.inactive:
                item.setTextColor(QtGui.QColor('red'))
            if variable.color != None:  # only variables that are selected have a color
                item.setBackgroundColor(QtGui.QColor(*variable.color))
            variable.items = [ item ]
            table.setItem(nRow, 0, item)

            item = QtGui.QTableWidgetItem()
            if variable.numeric:
                props = 'Min:%s, Max=%s' % (variable.min, variable.max)
            else:
                props = 'Text with %s values' % len(variable.list)
            item.setText(props)     # Variable's properties
            if variable.color != None:  # only variables that are selected have a color
                item.setBackgroundColor(QtGui.QColor(*variable.color))
            variable.items.append(item)
            table.setItem(nRow, 1, item)
            nRow += 1
    table.clearSelection()          # restore color from blue (selected)
    table.setSortingEnabled(True)
    table.sortItems(0)              # sort by col 0 (name) to start with
    table.resizeColumnsToContents()

# a variable name was clicked in a table 
def itemClicked(item):
    for variable in variables:      # find item that was clicked
        if item in variable.items:
            break
    else:                           # this should never happen
        displayStatus('Please click on a variable')
        return

    if variable.selected:
        variable.selected = False   # flip it off
        availColors.append(variable.color)      # return color to end of list of available availColors
        variable.color = None
        variable.axis = None        # discard AxisItem
        variable.vb = None          # discard viewBox
    else:
        if len(availColors) == 0:   # no more colors
            displayStatus('You are viewing too many variables.  Kindly restrain yourself :-)')
            return
        variable.selected = True
        variable.color = availColors.pop()      # get last color
        # move variable to end of list
        # this causes the variable that was selected first to get the column on the right
        variables.remove(variable)  # move variable to end of list
        variables.append(variable)
    displayAll()		# update both tables and plot

# "Hide Inactive" checkbox was clicked
def checkedStateChanged(item=None):
    hideInactive = ui.checkBoxHideInactive.isChecked()
    displayVariables(table=ui.varUnselectedTable, selected=False, hideInactive=hideInactive)

# view has resized; update auxiliary views to match
def updateViews():
    for variable in variables:
        if variable.selected:
            variable.vb.setGeometry(plotItem.vb.sceneBoundingRect())

# plot all selected variables
def displayPlot():
    if timer == None:       # timer will be none if no file data is available, typically when bad file opened
        return
    gl = ui.graphicsLayoutWidget
    gl.clear()              # try to remove previously added items 
    scene = gl.scene()      # somehow, clear() doesn't remove some added plots in scene()
    for item in scene.items():
        if not isinstance(item, pg.GraphicsLayout):     # leave one frame
            scene.removeItem(item)

    global plotItem
    plotItem = None
    col = 0                     # axis column in graphicsLayoutWidget
    for variable in variables:
        if variable.selected:
            vb = pg.ViewBox()
            vb.addItem(pg.PlotCurveItem(timer.values, variable.displayValues, name=variable.name, pen=variable.color))
            variable.vb = vb
    
            axis = pg.AxisItem('right') if variable.numeric else TextAxisItem('right')
            color = '#'+''.join('%02x' % i for i in variable.color)     # setLabel() does not work with color tuple
            axis.setLabel(variable.name, color=color)
            variable.axis = axis

            col += 1
            if plotItem == None:            # set up base item
                plotItem = pg.PlotItem(viewBox=vb, axisItems={'left' : axis})
                plotItem.showGrid(x=True, y=True, alpha=0.75)
                plotItem.setLabel('bottom', 'Time', 'Sec')
                gl.addItem(plotItem, row=2, col=col, rowspan=1, colspan=1)  # add plotitem to layout
                vb.sigResized.connect(updateViews)      # updates when resized
            else:
                gl.addItem(axis, row=2, col=col,  rowspan=1, colspan=1) # add axis to layout
                gl.scene().addItem(vb)      # add viewboxes to layout 
                axis.linkToView(vb)         # link axis with viewboxes
                vb.setXLink(plotItem.vb)    # link viewboxes
                vb.enableAutoRange()        # axis=pg.ViewBox.XYAxes, enable=True

# displays plot and variable tables
def displayAll():
    hideInactive = ui.checkBoxHideInactive.isChecked()  # could call checkedStateChanged()
    displayPlot()
    displayVariables(table=ui.varSelectedTable, selected=True, hideInactive=False)
    displayVariables(table=ui.varUnselectedTable, selected=False, hideInactive=hideInactive)

# display line in status bar at bottom of screen
def displayStatus(msg):
    mainWindow.statusBar().showMessage(msg)

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
def sysExit():
    sys.exit()

# button for compress Y axis
# disabled, causes divide by 0 exceptions
def buttonCompressY():
    gl = ui.graphicsLayoutWidget
    if ui.buttonCompressY.text() == 'Compress Y Axis':
        gl.setLogMode(False, True)
        ui.buttonCompressY.setText('Restore Y Axis')
    else:   # Restore Y Axis
        gl.setLogMode(False, False)
        ui.buttonCompressY.setText('Compress Y Axis')

# button for Reset Plot
def buttonReset():
    displayPlot()

# connect display items with callback functions
# plot resize event is connected each time a new plot is drawn
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

def main():
    global mainWindow, ui, gl
    app = QtGui.QApplication(sys.argv)
    mainWindow =  QtGui.QMainWindow()
    ui = uiPlotView.Ui_MainWindow()
    ui.setupUi(mainWindow)

    ag = app.desktop().availableGeometry(-1)
    mainWindow.resize(ag.width()-10, ag.height()-40)   # magic val for windows app bar

    connectAll()

    # pick up command line param, if present
    filename = getFileName() if len(sys.argv) <= 1 else sys.argv[1]
    data = readFile(filename)
    numLines = parseFile(data)
    displayStatus('File: %s, %s lines' % (filename, numLines))
    displayAll()

    mainWindow.show()
    sys.exit(app.exec_())

#####################
if __name__ == "__main__":
    main()