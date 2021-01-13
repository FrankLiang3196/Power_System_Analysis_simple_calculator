'''
Power System Analysis
Author: 梁飞，单士磊，蒋奕琛
Date: 2021.1.13
本程序仅用于课堂展示
'''


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 299)
        self.TransChoose = QtWidgets.QDialogButtonBox(Dialog)
        self.TransChoose.setGeometry(QtCore.QRect(-40, 100, 341, 32))
        self.TransChoose.setOrientation(QtCore.Qt.Horizontal)
        self.TransChoose.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.TransChoose.setObjectName("TransChoose")

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 150, 350, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet('background-color:rgba(255,255,255,0)')
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)


        self.retranslateUi(Dialog)
        self.TransChoose.accepted.connect(Dialog.accept)
        self.TransChoose.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.TransChoose.button(QtWidgets.QDialogButtonBox.Ok).setText('Known')
        self.TransChoose.button(QtWidgets.QDialogButtonBox.Cancel).setText('UnKnown')
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Transfomer Choose"))
        self.textBrowser.setText(_translate("Dialog",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Click OK if you have all the desired \nparameters (r,x,g,b);otherwise, click \ncancel.</span></p></body></html>"))

