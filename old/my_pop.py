# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myGUI/popup_params.ui'
#
# Created: Sun May 27 17:05:07 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(534, 257)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 518, 239))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setText(QtGui.QApplication.translate("Form", "feature_params", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.lkp_Table = QtGui.QTableWidget(self.widget)
        self.lkp_Table.setObjectName(_fromUtf8("lkp_Table"))
        self.lkp_Table.setColumnCount(1)
        self.lkp_Table.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "winSize", None, QtGui.QApplication.UnicodeUTF8))
        self.lkp_Table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "maxLevel", None, QtGui.QApplication.UnicodeUTF8))
        self.lkp_Table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Count", None, QtGui.QApplication.UnicodeUTF8))
        self.lkp_Table.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "EPS", None, QtGui.QApplication.UnicodeUTF8))
        self.lkp_Table.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "derivlam", None, QtGui.QApplication.UnicodeUTF8))
        self.lkp_Table.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.lkp_Table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.lkp_Table.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.lkp_Table.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.lkp_Table.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.lkp_Table.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.lkp_Table.setItem(4, 0, item)
        self.gridLayout.addWidget(self.lkp_Table, 1, 0, 1, 1)
        self.fp_Table = QtGui.QTableWidget(self.widget)
        self.fp_Table.setObjectName(_fromUtf8("fp_Table"))
        self.fp_Table.setColumnCount(1)
        self.fp_Table.setRowCount(4)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "max corners", None, QtGui.QApplication.UnicodeUTF8))
        self.fp_Table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "quality", None, QtGui.QApplication.UnicodeUTF8))
        self.fp_Table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "minDist", None, QtGui.QApplication.UnicodeUTF8))
        self.fp_Table.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "block", None, QtGui.QApplication.UnicodeUTF8))
        self.fp_Table.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.fp_Table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "500", None, QtGui.QApplication.UnicodeUTF8))
        self.fp_Table.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "0.001", None, QtGui.QApplication.UnicodeUTF8))
        self.fp_Table.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.fp_Table.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.fp_Table.setItem(3, 0, item)
        self.gridLayout.addWidget(self.fp_Table, 1, 1, 1, 1)
        self.pushClose = QtGui.QPushButton(self.widget)
        self.pushClose.setText(QtGui.QApplication.translate("Form", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushClose.setObjectName(_fromUtf8("pushClose"))
        self.gridLayout.addWidget(self.pushClose, 2, 0, 1, 2)
        self.label = QtGui.QLabel(self.widget)
        self.label.setText(QtGui.QApplication.translate("Form", "lk_params", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        item = self.lkp_Table.verticalHeaderItem(0)
        item = self.lkp_Table.verticalHeaderItem(1)
        item = self.lkp_Table.verticalHeaderItem(2)
        item = self.lkp_Table.verticalHeaderItem(3)
        item = self.lkp_Table.verticalHeaderItem(4)
        __sortingEnabled = self.lkp_Table.isSortingEnabled()
        self.lkp_Table.setSortingEnabled(False)
        item = self.lkp_Table.item(0, 0)
        item = self.lkp_Table.item(1, 0)
        item = self.lkp_Table.item(2, 0)
        item = self.lkp_Table.item(3, 0)
        item = self.lkp_Table.item(4, 0)
        self.lkp_Table.setSortingEnabled(__sortingEnabled)
        item = self.fp_Table.verticalHeaderItem(0)
        item = self.fp_Table.verticalHeaderItem(1)
        item = self.fp_Table.verticalHeaderItem(2)
        item = self.fp_Table.verticalHeaderItem(3)
        __sortingEnabled = self.fp_Table.isSortingEnabled()
        self.fp_Table.setSortingEnabled(False)
        item = self.fp_Table.item(0, 0)
        item = self.fp_Table.item(1, 0)
        item = self.fp_Table.item(2, 0)
        item = self.fp_Table.item(3, 0)
        self.fp_Table.setSortingEnabled(__sortingEnabled)
