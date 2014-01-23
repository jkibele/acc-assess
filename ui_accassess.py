# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_accassess.ui'
#
# Created: Thu Jan 23 11:54:05 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AccAssess(object):
    def setupUi(self, AccAssess):
        AccAssess.setObjectName(_fromUtf8("AccAssess"))
        AccAssess.resize(320, 377)
        self.verticalLayout = QtGui.QVBoxLayout(AccAssess)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(AccAssess)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.referenceComboBox = QtGui.QComboBox(AccAssess)
        self.referenceComboBox.setObjectName(_fromUtf8("referenceComboBox"))
        self.verticalLayout.addWidget(self.referenceComboBox)
        spacerItem = QtGui.QSpacerItem(20, 63, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(AccAssess)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.comparisonComboBox = QtGui.QComboBox(AccAssess)
        self.comparisonComboBox.setObjectName(_fromUtf8("comparisonComboBox"))
        self.verticalLayout.addWidget(self.comparisonComboBox)
        spacerItem1 = QtGui.QSpacerItem(20, 62, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.outFileLabel = QtGui.QLabel(AccAssess)
        self.outFileLabel.setObjectName(_fromUtf8("outFileLabel"))
        self.verticalLayout.addWidget(self.outFileLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.outFileLineEdit = QtGui.QLineEdit(AccAssess)
        self.outFileLineEdit.setObjectName(_fromUtf8("outFileLineEdit"))
        self.horizontalLayout.addWidget(self.outFileLineEdit)
        self.outFileSelectButton = QtGui.QPushButton(AccAssess)
        self.outFileSelectButton.setObjectName(_fromUtf8("outFileSelectButton"))
        self.horizontalLayout.addWidget(self.outFileSelectButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 32, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtGui.QDialogButtonBox(AccAssess)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AccAssess)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AccAssess.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AccAssess.reject)
        QtCore.QMetaObject.connectSlotsByName(AccAssess)

    def retranslateUi(self, AccAssess):
        AccAssess.setWindowTitle(QtGui.QApplication.translate("AccAssess", "AccAssess", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AccAssess", "Reference Map", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AccAssess", "Comparison Map", None, QtGui.QApplication.UnicodeUTF8))
        self.outFileLabel.setText(QtGui.QApplication.translate("AccAssess", "CSV Output File", None, QtGui.QApplication.UnicodeUTF8))
        self.outFileLineEdit.setPlaceholderText(QtGui.QApplication.translate("AccAssess", "error_matrix.csv", None, QtGui.QApplication.UnicodeUTF8))
        self.outFileSelectButton.setText(QtGui.QApplication.translate("AccAssess", "Select...", None, QtGui.QApplication.UnicodeUTF8))

