'''
Power System Analysis
Author: 梁飞，单士磊，蒋奕琛
Date: 2021.1.13
本程序仅用于课堂展示
'''


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LineChoose(object):
    def setupUi(self, LineChoose):
        LineChoose.setObjectName("LineChoose")
        LineChoose.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(LineChoose)
        self.buttonBox.setGeometry(QtCore.QRect(-50, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(LineChoose)
        self.textBrowser.setGeometry(QtCore.QRect(30, 150, 350, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet('background-color:rgba(255,255,255,0)')
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.retranslateUi(LineChoose)
        self.buttonBox.accepted.connect(LineChoose.accept)
        self.buttonBox.rejected.connect(LineChoose.reject)
        QtCore.QMetaObject.connectSlotsByName(LineChoose)

        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText('Known')
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText('UnKnown')

    def retranslateUi(self, LineChoose):
        _translate = QtCore.QCoreApplication.translate
        LineChoose.setWindowTitle(_translate("LineChoose", "LineChoose"))
        self.textBrowser.setHtml(_translate("Dialog",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Click OK if you have all the desired parameters (r,x,g,b);otherwise, click cancel.</span></p></body></html>"))

