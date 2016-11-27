# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\uiPlotView.ui'
#
# Created: Sat Nov 26 22:45:21 2016
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 661)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelTitle = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName(_fromUtf8("labelTitle"))
        self.verticalLayout.addWidget(self.labelTitle)
        self.fileProperties = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileProperties.sizePolicy().hasHeightForWidth())
        self.fileProperties.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fileProperties.setFont(font)
        self.fileProperties.setObjectName(_fromUtf8("fileProperties"))
        self.verticalLayout.addWidget(self.fileProperties)
        self.lineSeparator = QtGui.QFrame(self.centralwidget)
        self.lineSeparator.setFrameShape(QtGui.QFrame.HLine)
        self.lineSeparator.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineSeparator.setObjectName(_fromUtf8("lineSeparator"))
        self.verticalLayout.addWidget(self.lineSeparator)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayoutPlot = QtGui.QVBoxLayout(self.frame)
        self.verticalLayoutPlot.setObjectName(_fromUtf8("verticalLayoutPlot"))
        self.verticalLayout.addWidget(self.frame)
        self.plotLayout = QtGui.QVBoxLayout()
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.verticalLayout.addLayout(self.plotLayout)
        self.lineSeparator_2 = QtGui.QFrame(self.centralwidget)
        self.lineSeparator_2.setFrameShape(QtGui.QFrame.HLine)
        self.lineSeparator_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineSeparator_2.setObjectName(_fromUtf8("lineSeparator_2"))
        self.verticalLayout.addWidget(self.lineSeparator_2)
        self.varTable = QtGui.QTableWidget(self.centralwidget)
        self.varTable.setObjectName(_fromUtf8("varTable"))
        self.varTable.setColumnCount(3)
        self.varTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.varTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.varTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.varTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.varTable)
        self.horizontalLayoutButtons = QtGui.QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName(_fromUtf8("horizontalLayoutButtons"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem)
        self.buttonAudit = QtGui.QPushButton(self.centralwidget)
        self.buttonAudit.setObjectName(_fromUtf8("buttonAudit"))
        self.horizontalLayoutButtons.addWidget(self.buttonAudit)
        self.buttonCancel = QtGui.QPushButton(self.centralwidget)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.horizontalLayoutButtons.addWidget(self.buttonCancel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayoutButtons)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labelTitle.setText(_translate("MainWindow", "Telemetry Log Viewer", None))
        self.fileProperties.setText(_translate("MainWindow", "File: name", None))
        item = self.varTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Variable", None))
        item = self.varTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Properties", None))
        item = self.varTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Color", None))
        self.buttonAudit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Review and Audit the calculation of ratings for awards</p></body></html>", None))
        self.buttonAudit.setText(_translate("MainWindow", "Filter", None))
        self.buttonCancel.setToolTip(_translate("MainWindow", "<html><head/><body><p>Return to previous screen</p></body></html>", None))
        self.buttonCancel.setText(_translate("MainWindow", "Reset", None))

