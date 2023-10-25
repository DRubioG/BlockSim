# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BlockSim_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BlockSim(object):
    def setupUi(self, BlockSim):
        BlockSim.setObjectName("BlockSim")
        BlockSim.resize(400, 144)
        self.label = QtWidgets.QLabel(BlockSim)
        self.label.setGeometry(QtCore.QRect(20, 35, 31, 19))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(BlockSim)
        self.lineEdit.setGeometry(QtCore.QRect(60, 30, 201, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_search = QtWidgets.QPushButton(BlockSim)
        self.pushButton_search.setGeometry(QtCore.QRect(280, 30, 100, 27))
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_simulation = QtWidgets.QPushButton(BlockSim)
        self.pushButton_simulation.setGeometry(QtCore.QRect(10, 100, 100, 27))
        self.pushButton_simulation.setObjectName("pushButton_simulation")
        self.pushButton_c_export = QtWidgets.QPushButton(BlockSim)
        self.pushButton_c_export.setGeometry(QtCore.QRect(130, 100, 100, 27))
        self.pushButton_c_export.setObjectName("pushButton_c_export")
        self.pushButton_python_export = QtWidgets.QPushButton(BlockSim)
        self.pushButton_python_export.setGeometry(QtCore.QRect(250, 100, 131, 27))
        self.pushButton_python_export.setObjectName("pushButton_python_export")

        self.retranslateUi(BlockSim)
        QtCore.QMetaObject.connectSlotsByName(BlockSim)

    def retranslateUi(self, BlockSim):
        _translate = QtCore.QCoreApplication.translate
        BlockSim.setWindowTitle(_translate("BlockSim", "BlockSim"))
        self.label.setText(_translate("BlockSim", "File"))
        self.pushButton_search.setText(_translate("BlockSim", "Search"))
        self.pushButton_simulation.setText(_translate("BlockSim", "Simulation"))
        self.pushButton_c_export.setText(_translate("BlockSim", "C export"))
        self.pushButton_python_export.setText(_translate("BlockSim", "Python export"))
