
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from ui import uiPlotView
import sys

class TextAxisItem(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        print 'tickString', values, scale, spacing
        valueList = ['A', 'B', 'C', 'D', 'E', 'F']
        ret = []
        for v in values:
            i = int(v)
            s = valueList[i] if i >= 0  and  i < len(valueList) else ''
            ret.append(s)
        return ret

## view has resized; update auxiliary views to match
def updateViews():
    print 'updateViews'
    v2.setGeometry(v1.sceneBoundingRect())
    v3.setGeometry(v1.sceneBoundingRect())
    v4.setGeometry(v1.sceneBoundingRect())
    v5.setGeometry(v1.sceneBoundingRect())
    v6.setGeometry(v1.sceneBoundingRect())

#===========================
app = QtGui.QApplication(sys.argv)
mainWindow =  QtGui.QMainWindow()
ui = uiPlotView.Ui_MainWindow()
ui.setupUi(mainWindow)

ag = app.desktop().availableGeometry(-1)
#mainWindow.resize(ag.width()-10, ag.height()-40)   # magic val for windows app bar

# layout
l = ui.graphicsLayoutWidget

# Axis
a2 = pg.AxisItem("left")
a3 = TextAxisItem("left")
a4 = pg.AxisItem("left")
a5 = pg.AxisItem("left")
a6 = pg.AxisItem("left")

# ViewBoxes
v2 = pg.ViewBox()
v3 = pg.ViewBox()
v4 = pg.ViewBox()
v5 = pg.ViewBox()
v6 = pg.ViewBox()

# add axis to layout
## watch the col parameter here for the position
l.addItem(a2, row = 2, col = 5,  rowspan=1, colspan=1)
l.addItem(a3, row = 2, col = 4,  rowspan=1, colspan=1)
l.addItem(a4, row = 2, col = 3,  rowspan=1, colspan=1)
l.addItem(a5, row = 2, col = 2,  rowspan=1, colspan=1)
l.addItem(a6, row = 2, col = 1,  rowspan=1, colspan=1)

# plotitem and viewbox
## at least one plotitem is used whioch holds its own viewbox and left axis
pI = pg.PlotItem()
v1 = pI.vb # reference to viewbox of the plotitem
l.addItem(pI, row = 2, col = 6,  rowspan=1, colspan=1) # add plotitem to layout

# add viewboxes to layout 
l.scene().addItem(v2)
l.scene().addItem(v3)
l.scene().addItem(v4)
l.scene().addItem(v5)
l.scene().addItem(v6)

# link axis with viewboxes
a2.linkToView(v2)
a3.linkToView(v3)
a4.linkToView(v4)
a5.linkToView(v5)
a6.linkToView(v6)

# link viewboxes
v2.setXLink(v1)
v3.setXLink(v2)
v4.setXLink(v3)
v5.setXLink(v4)
v6.setXLink(v5)

# axes labels
pI.getAxis("left").setLabel('axis 1 in ViewBox of PlotItem', color='#FFFFFF')
a2.setLabel('axis 2 in Viewbox 2', color='#2E2EFE')
a3.setLabel('axis 3 in Viewbox 3', color='#2EFEF7')
a4.setLabel('axis 4 in Viewbox 4', color='#2EFE2E')
a5.setLabel('axis 5 in Viewbox 5', color='#FFFF00')
a6.setLabel('axis 6 in Viewbox 6', color='#FE2E64')


# data
x = [1,2,3,4,5,6]
y1 = [0,4,6,8,10,4]
y2 = [0,5,7,9,11,3]
y3 = [0,1,2,3,4,5]
y4 = [0,8,0.3,0.4,2,5]
y5 = [0,1,6,4,2,1]
y6 = [0,0.2,0.3,0.4,0.5,0.6]

# plot
v1.addItem(pg.PlotCurveItem(x, y1, pen='#FFFFFF'))
v2.addItem(pg.PlotCurveItem(x, y2, pen='#2E2EFE'))
v3.addItem(pg.PlotCurveItem(x, y3, pen='#2EFEF7'))
v4.addItem(pg.PlotCurveItem(x, y4, pen='#2EFE2E'))
v5.addItem(pg.PlotCurveItem(x, y5, pen='#FFFF00'))
v6.addItem(pg.PlotCurveItem(x, y6, pen='#FE2E64'))

# updates when resized
v1.sigResized.connect(updateViews)

# autorange once to fit views at start
v2.enableAutoRange()        # axis= pg.ViewBox.XYAxes, enable=True
v3.enableAutoRange()
v4.enableAutoRange()
v5.enableAutoRange()
v6.enableAutoRange()

updateViews()

mainWindow.show()
sys.exit(app.exec_())