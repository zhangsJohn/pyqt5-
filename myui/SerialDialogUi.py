# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\zhangs\Documents\Qt_Projects\Python\MyProject\Spec2.0\myui\SerialDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SrDialog(object):
    def setupUi(self, SrDialog):
        SrDialog.setObjectName("SrDialog")
        SrDialog.resize(203, 178)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SrDialog.sizePolicy().hasHeightForWidth())
        SrDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(SrDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(SrDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.portCB = QtWidgets.QComboBox(SrDialog)
        self.portCB.setObjectName("portCB")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.portCB)
        self.label_2 = QtWidgets.QLabel(SrDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.baudRateCB = QtWidgets.QComboBox(SrDialog)
        self.baudRateCB.setObjectName("baudRateCB")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.baudRateCB)
        self.label_3 = QtWidgets.QLabel(SrDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.stopBitCB = QtWidgets.QComboBox(SrDialog)
        self.stopBitCB.setObjectName("stopBitCB")
        self.stopBitCB.addItem("")
        self.stopBitCB.addItem("")
        self.stopBitCB.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stopBitCB)
        self.label_4 = QtWidgets.QLabel(SrDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dataBitCB = QtWidgets.QComboBox(SrDialog)
        self.dataBitCB.setObjectName("dataBitCB")
        self.dataBitCB.addItem("")
        self.dataBitCB.addItem("")
        self.dataBitCB.addItem("")
        self.dataBitCB.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dataBitCB)
        self.label_5 = QtWidgets.QLabel(SrDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.testCB = QtWidgets.QComboBox(SrDialog)
        self.testCB.setObjectName("testCB")
        self.testCB.addItem("")
        self.testCB.addItem("")
        self.testCB.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.testCB)
        self.label_6 = QtWidgets.QLabel(SrDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.timeOutEt = QtWidgets.QLineEdit(SrDialog)
        self.timeOutEt.setObjectName("timeOutEt")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.timeOutEt)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SrDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SrDialog)
        self.buttonBox.accepted.connect(SrDialog.accept)
        self.buttonBox.rejected.connect(SrDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SrDialog)

    def retranslateUi(self, SrDialog):
        _translate = QtCore.QCoreApplication.translate
        SrDialog.setWindowTitle(_translate("SrDialog", "Dialog"))
        self.label.setText(_translate("SrDialog", "串口选择"))
        self.label_2.setText(_translate("SrDialog", "波特率"))
        self.label_3.setText(_translate("SrDialog", "停止位"))
        self.stopBitCB.setItemText(0, _translate("SrDialog", "1"))
        self.stopBitCB.setItemText(1, _translate("SrDialog", "1.5"))
        self.stopBitCB.setItemText(2, _translate("SrDialog", "2"))
        self.label_4.setText(_translate("SrDialog", "数据位"))
        self.dataBitCB.setItemText(0, _translate("SrDialog", "8"))
        self.dataBitCB.setItemText(1, _translate("SrDialog", "7"))
        self.dataBitCB.setItemText(2, _translate("SrDialog", "6"))
        self.dataBitCB.setItemText(3, _translate("SrDialog", "5"))
        self.label_5.setText(_translate("SrDialog", "奇偶校验"))
        self.testCB.setItemText(0, _translate("SrDialog", "None"))
        self.testCB.setItemText(1, _translate("SrDialog", "Even"))
        self.testCB.setItemText(2, _translate("SrDialog", "Odd"))
        self.label_6.setText(_translate("SrDialog", "timeOut"))
        self.timeOutEt.setText(_translate("SrDialog", "2"))
