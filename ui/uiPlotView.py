# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\uiPlotView.ui'
#
# Created: Thu Dec 01 18:44:10 2016
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
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
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
        self.verticalLayout_3.addWidget(self.labelTitle)
        self.lineSeparator_3 = QtGui.QFrame(self.centralwidget)
        self.lineSeparator_3.setFrameShape(QtGui.QFrame.HLine)
        self.lineSeparator_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineSeparator_3.setObjectName(_fromUtf8("lineSeparator_3"))
        self.verticalLayout_3.addWidget(self.lineSeparator_3)
        self.graphicsLayout = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsLayout.setObjectName(_fromUtf8("graphicsLayout"))
        self.verticalLayout_3.addWidget(self.graphicsLayout)
        self.horizontalLayoutButtons = QtGui.QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName(_fromUtf8("horizontalLayoutButtons"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem)
        self.buttonCompressY = QtGui.QPushButton(self.centralwidget)
        self.buttonCompressY.setObjectName(_fromUtf8("buttonCompressY"))
        self.horizontalLayoutButtons.addWidget(self.buttonCompressY)
        self.buttonReset = QtGui.QPushButton(self.centralwidget)
        self.buttonReset.setObjectName(_fromUtf8("buttonReset"))
        self.horizontalLayoutButtons.addWidget(self.buttonReset)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayoutButtons)
        self.lineSeparator_2 = QtGui.QFrame(self.centralwidget)
        self.lineSeparator_2.setFrameShape(QtGui.QFrame.HLine)
        self.lineSeparator_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineSeparator_2.setObjectName(_fromUtf8("lineSeparator_2"))
        self.verticalLayout_3.addWidget(self.lineSeparator_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelTitle_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle_2.sizePolicy().hasHeightForWidth())
        self.labelTitle_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTitle_2.setFont(font)
        self.labelTitle_2.setObjectName(_fromUtf8("labelTitle_2"))
        self.horizontalLayout_2.addWidget(self.labelTitle_2)
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.varSelectedTable = QtGui.QTableWidget(self.centralwidget)
        self.varSelectedTable.setObjectName(_fromUtf8("varSelectedTable"))
        self.varSelectedTable.setColumnCount(2)
        self.varSelectedTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.varSelectedTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.varSelectedTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.varSelectedTable)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelTitle_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle_3.sizePolicy().hasHeightForWidth())
        self.labelTitle_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTitle_3.setFont(font)
        self.labelTitle_3.setObjectName(_fromUtf8("labelTitle_3"))
        self.horizontalLayout.addWidget(self.labelTitle_3)
        self.checkBoxHideInactive = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxHideInactive.setFont(font)
        self.checkBoxHideInactive.setChecked(True)
        self.checkBoxHideInactive.setObjectName(_fromUtf8("checkBoxHideInactive"))
        self.horizontalLayout.addWidget(self.checkBoxHideInactive)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.varUnselectedTable = QtGui.QTableWidget(self.centralwidget)
        self.varUnselectedTable.setObjectName(_fromUtf8("varUnselectedTable"))
        self.varUnselectedTable.setColumnCount(2)
        self.varUnselectedTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.varUnselectedTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.varUnselectedTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.varUnselectedTable)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtGui.QAction(MainWindow)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHow_to_pick_your_nose = QtGui.QAction(MainWindow)
        self.actionHow_to_pick_your_nose.setObjectName(_fromUtf8("actionHow_to_pick_your_nose"))
        self.actionGeneral_Help = QtGui.QAction(MainWindow)
        self.actionGeneral_Help.setObjectName(_fromUtf8("actionGeneral_Help"))
        self.actionHelp_with_Plots = QtGui.QAction(MainWindow)
        self.actionHelp_with_Plots.setObjectName(_fromUtf8("actionHelp_with_Plots"))
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionGeneral_Help)
        self.menuHelp.addAction(self.actionHelp_with_Plots)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionHow_to_pick_your_nose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labelTitle.setText(_translate("MainWindow", "Telemetry Log Viewer", None))
        self.buttonCompressY.setToolTip(_translate("MainWindow", "<html><head/><body><p>Make Y Axis Log10</p></body></html>", None))
        self.buttonCompressY.setText(_translate("MainWindow", "Compress Y Axis", None))
        self.buttonReset.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click Reset to adjust axis scales to display all plots.</p></body></html>", None))
        self.buttonReset.setText(_translate("MainWindow", "Reset Plot", None))
        self.labelTitle_2.setText(_translate("MainWindow", "Displayed variables", None))
        self.checkBox_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Come back later for this</p></body></html>", None))
        self.checkBox_2.setText(_translate("MainWindow", "Animate", None))
        self.varSelectedTable.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click on a variable to remove it from the display list.  The color of each variable is the color of the variable\'s plot line.</p></body></html>", None))
        item = self.varSelectedTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Variable", None))
        item = self.varSelectedTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Properties", None))
        self.labelTitle_3.setText(_translate("MainWindow", "Available to display", None))
        self.checkBoxHideInactive.setToolTip(_translate("MainWindow", "<html><head/><body><p>Inactive variables are those that do not change.  They are colored red.</p></body></html>", None))
        self.checkBoxHideInactive.setText(_translate("MainWindow", "Hide Inactive", None))
        self.varUnselectedTable.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click on a variable to display it.  Inactive variabled are colored red.  They do not change values.</p></body></html>", None))
        item = self.varUnselectedTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Variable", None))
        item = self.varUnselectedTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Properties", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout.setText(_translate("MainWindow", "About this version", None))
        self.actionHow_to_pick_your_nose.setText(_translate("MainWindow", "How to pick your nose", None))
        self.actionGeneral_Help.setText(_translate("MainWindow", "General Help", None))
        self.actionHelp_with_Plots.setText(_translate("MainWindow", "Help with Plots", None))

