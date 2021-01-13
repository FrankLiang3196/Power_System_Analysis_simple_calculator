'''
Power System Analysis
Author: 梁飞，单士磊，蒋奕琛
Date: 2021.1.13
本程序仅用于课堂展示
'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TransParaKnown_2(object):
    def setupUi(self, TransParaKnown_2):
        TransParaKnown_2.setObjectName("TransParaKnown_2")
        TransParaKnown_2.setEnabled(True)
        TransParaKnown_2.resize(600,300)
        self.buttonBox = QtWidgets.QDialogButtonBox(TransParaKnown_2)
        self.buttonBox.setGeometry(QtCore.QRect(90, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(TransParaKnown_2)
        self.widget.setGeometry(QtCore.QRect(10, 90, 550, 53))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.TransParaKnown = QtWidgets.QLabel(self.widget)
        self.TransParaKnown.setObjectName("TransParaKnown")
        self.verticalLayout.addWidget(self.TransParaKnown)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ParaEdit = QtWidgets.QLineEdit(self.widget)
        self.ParaEdit.setObjectName("ParaEdit")
        self.verticalLayout_2.addWidget(self.ParaEdit)
        self.LocationEdit = QtWidgets.QLineEdit(self.widget)
        self.LocationEdit.setObjectName("LocationEdit")
        self.verticalLayout_2.addWidget(self.LocationEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.retranslateUi(TransParaKnown_2)
        self.buttonBox.accepted.connect(TransParaKnown_2.accept)
        self.buttonBox.rejected.connect(TransParaKnown_2.reject)
        QtCore.QMetaObject.connectSlotsByName(TransParaKnown_2)

    def retranslateUi(self, TransParaKnown_2):
        _translate = QtCore.QCoreApplication.translate
        TransParaKnown_2.setWindowTitle(_translate("TransParaKnown_2", "Transformer"))
        self.TransParaKnown.setText(_translate("TransParaKnown_2", "Parameters:"))
        self.label_2.setText(_translate("TransParaKnown_2", "  Location:"))
        self.label.setText(_translate("TransParaKnown_2", "r(ohm),x(ohm),b(s),g(s)"))
        self.label_3.setText(_translate("TransParaKnown_2", "(x,y)"))

        self.ParaEdit.setToolTip('Set the r,x,b,g of the transformer.')
        self.ParaEdit.setStatusTip('Set the r,x,b,g of the transformer.')
        self.LocationEdit.setToolTip('Set the location of the line.')
        self.LocationEdit.setStatusTip('Set the location of the line.')


