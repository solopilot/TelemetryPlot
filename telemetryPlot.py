'''
Created on Nov 26, 2016

@author: solo

Booleans are converted to 1.0 or 0.0
xlrd does not distinguish between float and ints
also, pyqtgraph displays arrays of floats, so everything is in float
'''
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
import sys
from ui import uiPlotView
import version

# globals
variables = []      # list of Variables, all recorded data is read in here
ui = None



# Variable represents one column in the recorded data
class Variable:
    def __init__(self, name, column):
        self.name = name        # name from header line
        self.column = column    # column index
        self.numeric = False    # plottable
        self.values = []        # list of recorded values for this variable
        self.max = ''           # max value: empty
        self.min = ''
        self.constant = True    # is the value changing or not
        self.selected = False   # true if checkbox is checked
        self.item = None        # checkbox item with variable's name

    # value is a string
    def addValue(self, value):
        try:                    # check if this is an int or float value
            value = float(value)
        except:
            pass                # leave it as a string
        self.values.append(value)

# data must be lines separated by '\n'
# each line must be comma or tab separated variables
# delim will be ',' or '\t'
def parseFile(data, delim):
    numLines = 0
    lines = data.split('\n')
    for line in lines:
        fields = line.strip().split(delim)
        if len(fields) > 1  and  not fields[0].startswith('#'):
            if numLines == 0:       # first line is the header
                parseHeader(fields)
            else:
                parseData(fields)
            numLines += 1
    return numLines

# pick up variable names in header line
def parseHeader(fields):
    for col, name in enumerate(fields):     # fields is list of variable names
        if name == '':                      # blank?
            name = 'variable %s' % col
        variable = Variable(name, col)
        variables.append(variable)

def parseData(fields):
    for col, value in enumerate(fields):    # fields is list of variable values
        variable = variables[col]
        variable.addValue(value)

# booleans get converted to 1 & 0
# xlrd cannot distinguish between ints and floats
def parseXLStoCSV(fileName):
    import xlrd
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

# returns number of variables that can be plotted
def massageData():
    for variable in variables:
        try:
            variable.max = max(variable.values)
            variable.min = min(variable.values)
            sum(variable.values)                # sum will crash if not numeric
            variable.numeric = True
        except:
            pass
        variable.constant = variable.max == variable.min    # non changing
        variable.empty = variable.constant  and  variable.max == ''

def displayVars():
    table = ui.varTable
    count = sum(1 for variable in variables[1:] if variable.numeric)
    table.setRowCount(count)
    table.setSortingEnabled(False)
    n = 0
    for variable in variables[1:]:  # skip timer
        if variable.numeric:
            item = QtGui.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Checked if variable.selected else QtCore.Qt.Unchecked)
            item.setText(variable.name)
            if variable.constant:
                item.setTextColor(QtGui.QColor('red'))
            variable.item = item
            table.setItem(n, 0, item)

            item = QtGui.QTableWidgetItem()
            item.setText('Min:%s, Max=%s' % (variable.min, variable.max))
            table.setItem(n, 1, item)
            n += 1
    table.setSortingEnabled(True)
    table.resizeColumnsToContents()
    table.itemClicked.connect(itemClicked)

def itemClicked(item):
    for variable in variables:
        if variable.item == item:
            break
    else:
        print 'itemClicked: item not found!!!'
        return
    variable.selected = not variable.selected
    item.setCheckState(QtCore.Qt.Checked if variable.selected else QtCore.Qt.Unchecked)
    displayPlot()

def displayPlot():
    widget.clear()
    count = sum(1 for variable in variables[1:] if variable.selected)
    i = 0
    for variable in variables[1:]:    # skip first
        if variable.selected:
            widget.plot(variables[0].values, variable.values, name=variable.name, pen=(i, count))
            i += 1

#####################
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow =  QtGui.QMainWindow()
    ui = uiPlotView.Ui_MainWindow()
    ui.setupUi(mainWindow)

    widget = pg.PlotWidget()
    ui.plotLayout.addWidget(widget)
    widget.showGrid(x=True, y=True, alpha=0.6)

    pg.setConfigOptions(antialias=True) # Enable antialiasing for prettier plots

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        fileExts = '*.csv *.tsv *.xls *.xlsx'
        filename = QtGui.QFileDialog.getOpenFileName(None, 'Open log file', '', 'Files (%s)' % fileExts)
        if filename in [None, '']:      # cancelled
            sys.exit()
        filename = str(filename)        # convert qstring to str

    parts = filename.lower().rsplit('.', 1) # convert .XLS to .xls
    if parts[-1] in ['xls', 'xlsx']:
        data = parseXLStoCSV(filename)  # convert to CSV
        delim = ','
    else:   # must be CSV file
        with open(filename, 'r') as f:
            data = f.read()             # read in the whole file
        delim = ',' if parts[-1] == 'csv' else '\t'

    numLines = parseFile(data, delim)
    ui.fileProperties.setText('File: %s, %s lines' % (filename, numLines))
    massageData()
    displayVars()
    displayPlot()
    mainWindow.show()
    sys.exit(app.exec_())