'''
Power System Analysis
Author: 梁飞，单士磊，蒋奕琛
Date: 2021.1.13
本程序仅用于课堂展示
'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LineParaKonwn(object):
    def setupUi(self, LineParaKonwn):
        LineParaKonwn.setObjectName("LineParaKonwn")
        LineParaKonwn.resize(600, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(LineParaKonwn)
        self.buttonBox.setGeometry(QtCore.QRect(90, 230, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(LineParaKonwn)
        self.widget.setGeometry(QtCore.QRect(10, 90, 550, 53))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LineParaEdit = QtWidgets.QLineEdit(self.widget)
        self.LineParaEdit.setObjectName("LineParaEdit")
        self.verticalLayout.addWidget(self.LineParaEdit)
        self.LocationEdit = QtWidgets.QLineEdit(self.widget)
        self.LocationEdit.setObjectName("LocationEdit")
        self.verticalLayout.addWidget(self.LocationEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.retranslateUi(LineParaKonwn)
        self.buttonBox.accepted.connect(LineParaKonwn.accept)
        self.buttonBox.rejected.connect(LineParaKonwn.reject)
        QtCore.QMetaObject.connectSlotsByName(LineParaKonwn)

    def retranslateUi(self, LineParaKonwn):
        _translate = QtCore.QCoreApplication.translate
        LineParaKonwn.setWindowTitle(_translate("LineParaKonwn", "Line"))
        self.label.setText(_translate("LineParaKonwn", " LineParameters:"))
        self.label_2.setText(_translate("LineParaKonwn", "       Location:"))
        self.label_3.setText(_translate("LineParaKonwn", "r(ohm),x(ohm),b(s),g(s)"))
        self.label_4.setText(_translate("LineParaKonwn", "(x,y)"))

        self.LineParaEdit.setToolTip('Set the parameters of the line, including the r,x,b,g.')
        self.LineParaEdit.setStatusTip('Set the parameters of the line, including the r,x,b,g.')
        self.LocationEdit.setToolTip('Set the location of the line in the form of(x,y).')
        self.LocationEdit.setStatusTip('Set the location of the line in the form of(x,y).')


