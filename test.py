'''
Created on Dec 1, 2016

@author: solo
'''
# -*- coding: utf-8 -*-
"""
Demonstrates a way to put multiple axes around a single plot. 

(This will eventually become a built-in feature of PlotItem)

"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from ui import uiPlotView
import sys


## view has resized; update auxiliary views to match
def updateViews():
    vb.setGeometry(pitem.vb.sceneBoundingRect())

app = QtGui.QApplication(sys.argv)
mainWindow =  QtGui.QMainWindow()
ui = uiPlotView.Ui_MainWindow()
ui.setupUi(mainWindow)

ag = app.desktop().availableGeometry(-1)
mainWindow.resize(ag.width()-10, ag.height()-40)   # magic val for windows app bar

widget = ui.plotWidget
widget.showGrid(x=True, y=True, alpha=0.75)
widget.setLabel('bottom', 'Time', 'Sec')
widget.setLabels(left='Numeric Y Value')

widget.plotItem.vb.sigResized.connect(updateViews)

pitem = widget.plotItem                 # same as widget.plotItem getPlotItem()

## create third ViewBox. 
## this time we need to create a new axis as well.
vb = pg.ViewBox()
axis = pg.AxisItem('right')
pitem.layout.addItem(axis, 2, 3)
pitem.scene().addItem(vb)
axis.linkToView(vb)
vb.setXLink(pitem)
axis.setZValue(-10000)
axis.setLabel('axis 3', color='#ff0000')

vb.setGeometry(pitem.vb.sceneBoundingRect())

pitem.plot([1,2,4,8,16,32])
vb.addItem(pg.PlotCurveItem([3200,1600,800,400,200,100], pen='r'))

mainWindow.show()
sys.exit(app.exec_())