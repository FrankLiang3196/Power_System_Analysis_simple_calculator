'''
Power System Analysis
Author: 梁飞，单士磊，蒋奕琛
Date: 2021.1.13
本程序仅用于课堂展示
'''


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculate(object):
    def setupUi(self, Calculate):
        Calculate.setObjectName("Calculate")
        Calculate.resize(1221, 882)
        self.buttonBox = QtWidgets.QDialogButtonBox(Calculate)
        self.buttonBox.setGeometry(QtCore.QRect(850, 850, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_4 = QtWidgets.QLabel(Calculate)
        self.label_4.setGeometry(QtCore.QRect(200, 700, 181, 61))
        self.label_4.setObjectName("label_4")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Calculate)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(370, 670, 591, 121))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LineLoss = QtWidgets.QTableWidget(self.gridLayoutWidget_3)
        self.LineLoss.setObjectName("LineLoss")
        self.LineLoss.setColumnCount(0)
        self.LineLoss.setRowCount(0)
        self.gridLayout_3.addWidget(self.LineLoss, 0, 0, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(Calculate)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(369, 69, 591, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.AdmittanceMatrix = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.AdmittanceMatrix.setObjectName("AdmittanceMatrix")
        self.AdmittanceMatrix.setColumnCount(0)
        self.AdmittanceMatrix.setRowCount(0)
        self.gridLayout.addWidget(self.AdmittanceMatrix, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Calculate)
        self.label.setGeometry(QtCore.QRect(110, 220, 251, 121))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Calculate)
        self.label_2.setGeometry(QtCore.QRect(180, 560, 181, 61))
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Calculate)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(370, 520, 591, 121))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BusVoltage = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.BusVoltage.setObjectName("BusVoltage")
        self.BusVoltage.setColumnCount(0)
        self.BusVoltage.setRowCount(0)
        self.gridLayout_2.addWidget(self.BusVoltage, 0, 0, 1, 1)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText('Output to file')


        self.retranslateUi(Calculate)
        self.buttonBox.accepted.connect(Calculate.accept)
        self.buttonBox.rejected.connect(Calculate.reject)
        QtCore.QMetaObject.connectSlotsByName(Calculate)

    def retranslateUi(self, Calculate):
        _translate = QtCore.QCoreApplication.translate
        Calculate.setWindowTitle(_translate("Calculate", "Result"))
        self.label_4.setText(_translate("Calculate", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">  Line Loss：</span></p></body></html>"))
        self.label.setText(_translate("Calculate", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Admittance Matrix: </span></p></body></html>"))
        self.label_2.setText(_translate("Calculate", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Bus Voltage:</span></p></body></html>"))
