'''
Power System Analysis
Author: 梁飞，单士磊，蒋奕琛
Date: 2021.1.13
本程序仅用于课堂展示
'''

import sys
# import traceback
import prettytable as pt
from PyQt5 import QtCore, QtGui, QtWidgets
from submenu import LineParaUnkown, LineParaKnown, LineChoose, TransChoose, TransParaUnknown
from submenu import TransParaKnown, BBusPara, CClear, Calculate
from SystemStructure import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(430, 30, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 130, 621, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.busBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.busBox.setObjectName("busBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.busBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.BuslistWidget = QtWidgets.QListWidget(self.busBox)
        self.BuslistWidget.setObjectName("BuslistWidget")
        self.verticalLayout_2.addWidget(self.BuslistWidget)
        self.AddBus = QtWidgets.QPushButton(self.busBox)
        self.AddBus.setObjectName("AddBus")
        self.verticalLayout_2.addWidget(self.AddBus)
        self.BusModifyBtn = QtWidgets.QPushButton(self.busBox)
        self.BusModifyBtn.setObjectName("BusModifyBtn")
        self.verticalLayout_2.addWidget(self.BusModifyBtn)
        self.DeleteBus = QtWidgets.QPushButton(self.busBox)
        self.DeleteBus.setObjectName("DeleteBus")
        self.verticalLayout_2.addWidget(self.DeleteBus)
        self.horizontalLayout.addWidget(self.busBox)
        self.transformerBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.transformerBox.setObjectName("transformerBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.transformerBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        # self.TextTransformer = QtWidgets.QTextBrowser(self.transformerBox)
        # self.TextTransformer.setObjectName("TextTransformer")
        # self.verticalLayout_3.addWidget(self.TextTransformer)
        self.TranslistWidget = QtWidgets.QListWidget(self.busBox)
        self.TranslistWidget.setObjectName("TranslistWidget")
        self.verticalLayout_3.addWidget(self.TranslistWidget)
        self.AddTransformer = QtWidgets.QPushButton(self.transformerBox)
        self.AddTransformer.setObjectName("AddTransformer")
        self.verticalLayout_3.addWidget(self.AddTransformer)
        self.TransModifyBtn = QtWidgets.QPushButton(self.busBox)
        self.TransModifyBtn.setObjectName("TransModifyBtn")
        self.verticalLayout_3.addWidget(self.TransModifyBtn)
        self.DeleteTransformer = QtWidgets.QPushButton(self.transformerBox)
        self.DeleteTransformer.setObjectName("DeleteTransformer")
        self.verticalLayout_3.addWidget(self.DeleteTransformer)
        self.horizontalLayout.addWidget(self.transformerBox)
        self.lineBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.lineBox.setObjectName("lineBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.lineBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        # self.TextLine = QtWidgets.QTextBrowser(self.lineBox)
        # self.TextLine.setObjectName("TextLine")
        # self.verticalLayout_4.addWidget(self.TextLine)
        self.LinelistWidget = QtWidgets.QListWidget(self.busBox)
        self.LinelistWidget.setObjectName("LinelistWidget")
        self.verticalLayout_4.addWidget(self.LinelistWidget)
        self.AddLine = QtWidgets.QPushButton(self.lineBox)
        self.AddLine.setObjectName("AddLine")
        self.verticalLayout_4.addWidget(self.AddLine)
        self.LineModifyBtn = QtWidgets.QPushButton(self.busBox)
        self.LineModifyBtn.setObjectName("LineModifyBtn")
        self.verticalLayout_4.addWidget(self.LineModifyBtn)
        self.DeleteLine = QtWidgets.QPushButton(self.lineBox)
        self.DeleteLine.setObjectName("DeleteLine")
        self.verticalLayout_4.addWidget(self.DeleteLine)
        self.horizontalLayout.addWidget(self.lineBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 180, 197, 229))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Load = QtWidgets.QPushButton(self.layoutWidget1)
        self.Load.setObjectName("Load")
        self.verticalLayout.addWidget(self.Load)
        self.Save = QtWidgets.QPushButton(self.layoutWidget1)
        self.Save.setObjectName("Save")
        self.verticalLayout.addWidget(self.Save)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.toolBox = QtWidgets.QGroupBox(self.layoutWidget1)
        self.toolBox.setObjectName("toolBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.toolBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.toolBox)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.toolBox)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_6.addWidget(self.lineEdit)
        self.SetVoltage = QtWidgets.QPushButton(self.toolBox)
        self.SetVoltage.setObjectName("SetVoltage")
        self.verticalLayout_6.addWidget(self.SetVoltage)
        self.Calculate = QtWidgets.QPushButton(self.toolBox)
        self.Calculate.setObjectName("Calculate")
        self.verticalLayout_6.addWidget(self.Calculate)
        self.verticalLayout_7.addWidget(self.toolBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ClearAll = QtWidgets.QPushButton(self.centralwidget)
        self.ClearAll.setGeometry(QtCore.QRect(790, 580, 93, 28))
        self.ClearAll.setObjectName("Clear All")

        QtWidgets.QToolTip.setFont(QtGui.QFont('Arial Black', 10))
        self.Load.setToolTip('Load the file from the expected position.')
        self.Load.setStatusTip('Load the file from the expected position.')
        self.lineEdit.setToolTip('Set the initial voltage.')
        self.lineEdit.setStatusTip('Set the initial voltage.')
        self.SetVoltage.setToolTip('The voltage you set will be read.')
        self.SetVoltage.setStatusTip('The voltage you set will be read.')
        self.Calculate.setToolTip('The data you previously set will be calculated.')
        self.Calculate.setStatusTip('The data you previously set will be calculated.')
        self.AddBus.setToolTip('After set the initial voltage you can add the parameters of bus.')
        self.AddBus.setStatusTip('After set the initial voltage you can add the parameters of bus.')
        self.DeleteBus.setToolTip('The last data you type in will be deleted.')
        self.DeleteBus.setStatusTip('The last data you type in will be deleted.')
        self.AddLine.setToolTip('After set the initial voltage you can add the parameters of line.')
        self.AddLine.setStatusTip('After set the initial voltage you can add the parameters of line.')
        self.DeleteLine.setToolTip('The last data you type in will be deleted.')
        self.DeleteLine.setStatusTip('The last data you type in will be deleted.')
        self.AddTransformer.setToolTip('After set the initial voltage you can add the parameters of transformer.')
        self.AddTransformer.setStatusTip('After set the initial voltage you can add the parameters of transformer.')
        self.DeleteTransformer.setToolTip('The last data you type in will be deleted.')
        self.DeleteTransformer.setStatusTip('The last data you type in will be deleted.')
        self.ClearAll.setToolTip('Clear all the data on this interface.')
        self.ClearAll.setStatusTip('Clear all the data on this interface.')


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 初始化PowerGrid
        self.powergrid = PowerGrid()

        # 定义计数器
        self.num_line = 1
        self.num_Trans = 1
        self.num_bus = 0

        #连接
        self.AddLine.clicked.connect(self.Line_Button)
        self.AddTransformer.clicked.connect(self.Trans_Button)
        self.AddBus.clicked.connect(self.Bus_button)
        self.SetVoltage.clicked.connect(self.Read_Voltage)
        self.DeleteBus.clicked.connect(self.Delete_Bus)
        self.DeleteLine.clicked.connect(self.Delete_Line)
        self.DeleteTransformer.clicked.connect(self.Delete_Trans)
        self.Save.clicked.connect(self.Save_button)
        self.Load.clicked.connect(self.Load_button)
        self.ClearAll.clicked.connect(self.Delete_All)
        self.Calculate.clicked.connect(self.Calculate_button)
        self.BusModifyBtn.clicked.connect(self.Bus_modify)
        self.TransModifyBtn.clicked.connect(self.Trans_modify)
        self.LineModifyBtn.clicked.connect(self.Line_modify)

    def Delete_All(self):
        Dialog = QtWidgets.QDialog()
        ui = CClear.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        # Dialog.exec_()
        rsp = Dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            self.powergrid = PowerGrid()
            self.clear()
        elif rsp == QtWidgets.QDialog.Rejected:
            pass

    def clear(self):
        self.num_line = 1
        self.num_Trans = 1
        self.num_bus = 0
        self.lineEdit.clear()
        # self.TextBus.clear()
        self.BuslistWidget.clear()
        # self.TextLine.clear()
        self.LinelistWidget.clear()
        # self.TextTransformer.clear()
        self.TranslistWidget.clear()

    def Read_Voltage(self):
        vol_str = self.lineEdit.text()
        try:
            voltage = float(vol_str)
            if not self.powergrid.V_initial:
                # self.TextBus.append("Bus" + str(self.num_bus) + '  Vθ\n')
                self.BuslistWidget.addItem("Bus" + str(self.num_bus) + '  Vθ')
                self.num_bus += 1

            self.powergrid.set_V(voltage, 0.0)
        except ValueError as e:
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'Invalid input. Please try again.')

    def Line_Button(self):
        Dialog = QtWidgets.QDialog()
        ui = LineChoose.Ui_LineChoose()
        ui.setupUi(Dialog)
        Dialog.show()
        #Dialog.exec_()
        rsp = Dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            self.Known_Button()
        elif rsp == QtWidgets.QDialog.Rejected:
            self.Unknown_Button()

    def Trans_Button(self):
        Dialog = QtWidgets.QDialog()
        ui = TransChoose.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        #Dialog.exec_()
        rsp = Dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            self.KnownT_Button()
        elif rsp == QtWidgets.QDialog.Rejected:
            self.UnknownT_Button()

    def Known_Button(self):
        Dialog = QtWidgets.QDialog()
        ui = LineParaKnown.Ui_LineParaKonwn()
        ui.setupUi(Dialog)
        Dialog.show()
        rsp = Dialog.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            try:
                loc_txt = ui.LocationEdit.text()
                para_txt = ui.LineParaEdit.text()
                line_para = tuple(map(float, para_txt.split(',')))
                location = tuple(map(int, loc_txt.split(',')))

                self.powergrid.add_line(location, Line(paraKnown=True, paras=line_para))
                self.LinelistWidget.addItem("Line" + str(self.num_line) + "  " + str(location))
                self.num_line += 1
            except ValueError as e:
                QtWidgets.QMessageBox.critical(Dialog, 'Error', 'Invalid input. Please try again.')
                # print('Invalid input. Please try again.' + e.args[0])

    def Unknown_Button(self):
        Dialog = QtWidgets.QDialog()
        ui = LineParaUnkown.Ui_LineParaUnkown()
        ui.setupUi(Dialog)
        Dialog.show()
        rsp = Dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            try:
                LineType = ui.lineTypeEdit.text()
                distance = tuple(map(float, ui.distenceEdit.text().split(',')))
                req = float(ui.reqEdit.text())
                n = int(ui.nEdit_5.text())
                length = float(ui.lengthEdit_3.text())
                loc_txt = ui.locationEdit_6.text()
                location = tuple(map(int, loc_txt.split(',')))

                self.powergrid.add_line(location, Line(paraKnown=False,
                                                       lineType=LineType, distance=distance, req=req, n=n, length=length))
                self.LinelistWidget.addItem("Line" + str(self.num_line) + "  " + str(location))
                self.num_line += 1
            except ValueError as e:
                QtWidgets.QMessageBox.critical(Dialog, 'Error', 'Invalid input. Please try again.')

    def Line_modify(self):
        try:
            n = self.LinelistWidget.selectedIndexes()[0].row()
            item = self.LinelistWidget.selectedItems()[0]
            if self.powergrid.line_list[n][1].paraKnown:
                Dialog = QtWidgets.QDialog()
                ui = LineParaKnown.Ui_LineParaKonwn()
                ui.setupUi(Dialog)

                line = self.powergrid.line_list[n]
                loc_txt = str(line[0][0]) + ',' + str(line[0][1])
                ui.LocationEdit.setText(loc_txt)
                paras_txt = str(line[1].get_paras()[0]) + ',' + str(line[1].get_paras()[1]) + ',' \
                            + str(line[1].get_paras()[2]) + ',' + str(line[1].get_paras()[3])
                ui.LineParaEdit.setText(paras_txt)
                Dialog.show()
                rsp = Dialog.exec_()
                if rsp == QtWidgets.QDialog.Accepted:
                    para_txt = ui.LineParaEdit.text()
                    loc_txt = ui.LocationEdit.text()
                    tran_para = tuple(map(float, para_txt.split(',')))
                    location = tuple(map(int, loc_txt.split(',')))

                    item.setText("Line" + str(n + 1) + "  " + str(location))
                    self.powergrid.delete_line(n)
                    self.powergrid.add_line(location, Transformer(paraKnown=True, paras=tran_para), seq=n)

            else:
                Dialog = QtWidgets.QDialog()
                ui = LineParaUnkown.Ui_LineParaUnkown()
                ui.setupUi(Dialog)

                line = self.powergrid.line_list[n]
                loc_txt = str(line[0][0]) + ',' + str(line[0][1])
                ui.locationEdit_6.setText(loc_txt)
                ui.lineTypeEdit.setText(str(line[1].lineType))
                ui.distenceEdit.setText(str(line[1].distance).strip('(').strip(')'))
                ui.reqEdit.setText(str(line[1].req))
                ui.nEdit_5.setText(str(line[1].n))
                ui.lengthEdit_3.setText(str(line[1].length))
                Dialog.show()
                rsp = Dialog.exec_()
                if rsp == QtWidgets.QDialog.Accepted:
                    LineType = ui.lineTypeEdit.text()
                    distance = tuple(map(float, ui.distenceEdit.text().split(',')))
                    req = float(ui.reqEdit.text())
                    n = int(ui.nEdit_5.text())
                    length = float(ui.lengthEdit_3.text())
                    loc_txt = ui.locationEdit_6.text()
                    location = tuple(map(int, loc_txt.split(',')))

                    item.setText("Line" + str(n + 1) + "  " + str(location))
                    self.powergrid.delete_line(n)
                    self.powergrid.add_line(location, Line(paraKnown=False,
                                                           lineType=LineType, distance=distance, req=req, n=n,
                                                           length=length))

        except IndexError as e:
            # 改！
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', e.args[0])
        except ValueError:
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'Invalid input. Please try again.')

    def KnownT_Button(self):
        Dialog = QtWidgets.QDialog()
        ui = TransParaKnown.Ui_TransParaKnown_2()
        ui.setupUi(Dialog)
        Dialog.show()
        rsp = Dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            try:
                para_txt = ui.ParaEdit.text()
                loc_txt = ui.LocationEdit.text()
                tran_para = tuple(map(float, para_txt.split(',')))
                location = tuple(map(int, loc_txt.split(',')))

                self.powergrid.add_transformer(location, Transformer(paraKnown=True, paras=tran_para))
                self.TranslistWidget.addItem("Transformer" + str(self.num_Trans) + "  " + str(location))
                # self.TextTransformer.append("Transformer" + str(self.num_Trans) + "  " + str(location) + '\n')
                self.num_Trans += 1
            except ValueError as e:
                pass

    def UnknownT_Button(self):
        Dialog = QtWidgets.QDialog()
        ui = TransParaUnknown.Ui_TransParaUnknown()
        ui.setupUi(Dialog)
        Dialog.show()
        rsp = Dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            try:
                Pk = float(ui.PkEdit.text())
                Uk = float(ui.UkEdit.text())
                Un = float(ui.UnEdit.text())
                Po = float(ui.PoEdit.text())
                Io = float(ui.IoEdit.text())
                ratio_txt = ui.ratioEdit.text()
                Sn = float(ui.SnEdit.text())
                loc_txt = ui.Location.text()
                location = tuple(map(int, loc_txt.split(',')))
                ratio = tuple(map(int, ratio_txt.split(',')))

                self.powergrid.add_transformer(location, Transformer(Pk=Pk, Uk=Uk, Un=Un, Po=Po,
                                                                     ratio=ratio, Io=Io, Sn=Sn))
                # self.TextTransformer.append("Transformer" + str(self.num_Trans) + "  " + str(location) + '\n')
                self.TranslistWidget.addItem("Transformer" + str(self.num_Trans) + "  " + str(location))
                self.num_Trans += 1
            except ValueError as e:
                pass

    def Trans_modify(self):
        try:
            n = self.TranslistWidget.selectedIndexes()[0].row()
            item = self.TranslistWidget.selectedItems()[0]

            if self.powergrid.transformer_list[n][1].paraKnown:
                Dialog = QtWidgets.QDialog()
                ui = TransParaKnown.Ui_TransParaKnown_2()
                ui.setupUi(Dialog)

                transformer = self.powergrid.transformer_list[n]
                loc_txt = str(transformer[0][0]) + ',' + str(transformer[0][1])
                ui.LocationEdit.setText(loc_txt)
                paras_txt = str(transformer[1].get_paras()[0]) + ',' + str(transformer[1].get_paras()[1]) + ',' \
                            + str(transformer[1].get_paras()[2]) + ',' + str(transformer[1].get_paras()[3])
                ui.ParaEdit.setText(paras_txt)
                Dialog.show()
                rsp = Dialog.exec_()
                if rsp == QtWidgets.QDialog.Accepted:
                    para_txt = ui.ParaEdit.text()
                    loc_txt = ui.LocationEdit.text()
                    tran_para = tuple(map(float, para_txt.split(',')))
                    location = tuple(map(int, loc_txt.split(',')))

                    item.setText("Transformer" + str(n + 1) + "  " + str(location))
                    self.powergrid.delete_transformer(n)
                    self.powergrid.add_transformer(location, Transformer(paraKnown=True, paras=tran_para), seq=n)

            else:
                Dialog = QtWidgets.QDialog()
                ui = TransParaUnknown.Ui_TransParaUnknown()
                ui.setupUi(Dialog)

                transformer = self.powergrid.transformer_list[n]
                loc_txt = str(transformer[0][0]) + ',' + str(transformer[0][1])
                ui.Location.setText(loc_txt)
                ui.PkEdit.setText(str(transformer[1].Pk))
                ui.UkEdit.setText(str(transformer[1].Uk))
                ui.UnEdit.setText(str(transformer[1].Un))
                ui.PoEdit.setText(str(transformer[1].Po))
                ui.IoEdit.setText(str(transformer[1].Io))
                ui.ratioEdit.setText(str(transformer[1].ratio[0]) + ',' + str(transformer[1].ratio[1]))
                ui.SnEdit.setText(str(transformer[1].Sn))
                Dialog.show()
                rsp = Dialog.exec_()
                if rsp == QtWidgets.QDialog.Accepted:
                    Pk = float(ui.PkEdit.text())
                    Uk = float(ui.UkEdit.text())
                    Un = float(ui.UnEdit.text())
                    Po = float(ui.PoEdit.text())
                    Io = float(ui.IoEdit.text())
                    ratio_txt = ui.ratioEdit.text()
                    Sn = float(ui.SnEdit.text())
                    loc_txt = ui.Location.text()
                    location = tuple(map(int, loc_txt.split(',')))
                    ratio = tuple(map(int, ratio_txt.split(',')))

                    item.setText("Transformer" + str(n + 1) + "  " + str(location))
                    self.powergrid.delete_transformer(n)
                    self.powergrid.add_transformer(location, Transformer(Pk=Pk, Uk=Uk, Un=Un, Po=Po,
                                                                         Io=Io, ratio=ratio, Sn=Sn), seq=n)

        except IndexError as e:
            # 改！
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', e.args[0])
        except ValueError:
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'Invalid input. Please try again.')

    def Bus_button(self):
        Dialog = QtWidgets.QDialog()
        ui = BBusPara.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        # Dialog.exec_()
        rsp = Dialog.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            try:
                BusType = ui.typetext.text()
                P = float(ui.Ptext.text())
                Q = float(ui.Qtext.text())
                V = float(ui.Vtext.text())
                k = float(ui.Ktext.text())

                if BusType == 'PQ':
                    # 改
                    self.powergrid.add_bus(P=P, Q=Q, k=k, busType=1)
                if BusType == 'PV':
                    self.powergrid.add_bus(P=P, V=V, k=k, busType=2)

                # self.TextBus.append("Bus" + str(self.num_bus) + "  " + BusType + '\n')
                self.BuslistWidget.addItem("Bus" + str(self.num_bus) + "  " + BusType)
                self.num_bus += 1
            except IndexError as e:
                # 改！
                QtWidgets.QMessageBox.critical(Dialog, 'Error', e.args[0])
            except ValueError:
                QtWidgets.QMessageBox.critical(Dialog, 'Error', 'Invalid input. Please try again.')

    def Bus_modify(self):
        Dialog = QtWidgets.QDialog()
        ui = BBusPara.Ui_Dialog()
        ui.setupUi(Dialog)
        try:
            n = self.BuslistWidget.selectedIndexes()[0].row()
            if n == 0:
                raise IndexError('Use Set Voltage to modify the Vθ bus.')
            bus = self.powergrid.char_matrix[n]
            ui.Ptext.setText(str(bus[3]))
            ui.Qtext.setText(str(bus[4]))
            ui.Vtext.setText(str(bus[5]))
            ui.Ktext.setText(str(bus[6]))
            if bus[0] == 1:
                ui.typetext.setText('PQ')
            elif bus[0] == 2:
                ui.typetext.setText('PV')
            Dialog.show()
            # Dialog.exec_()
            rsp = Dialog.exec_()

            if rsp == QtWidgets.QDialog.Accepted:
                BusType = ui.typetext.text()
                P = float(ui.Ptext.text())
                Q = float(ui.Qtext.text())
                V = float(ui.Vtext.text())
                k = float(ui.Ktext.text())

                if BusType == 'PQ':
                    # 改
                    new_bus_type = 1
                elif BusType == 'PV':
                    new_bus_type = 2
                else:
                    raise ValueError

                if new_bus_type != bus[0]:
                    raise Exception('Cannot change bus type.')
                elif new_bus_type == 1:
                    self.powergrid.delete_bus(n)
                    self.powergrid.add_bus(seq=n, P=P, Q=Q, k=k, busType=1)
                elif new_bus_type == 2:
                    self.powergrid.delete_bus(n)
                    self.powergrid.add_bus(seq=n, P=P, V=V, k=k, busType=2)

        except IndexError as e:
            # 改！
            QtWidgets.QMessageBox.critical(Dialog, 'Error', e.args[0])
            # print(traceback.print_exc())
        except ValueError:
            QtWidgets.QMessageBox.critical(Dialog, 'Error', 'Invalid input. Please try again.')
        except Exception as e:
            QtWidgets.QMessageBox.critical(Dialog, 'Error', e.args[0])

    def Delete_Bus(self):
        try:
            n = self.BuslistWidget.selectedIndexes()[0].row()
            self.powergrid.delete_bus(n)
            self.BuslistWidget.takeItem(n)
            # str = self.TextBus.toPlainText()
            # str = str[:-10]
            # self.TextBus.setText(str)
            self.num_bus -= 1
        except IndexError as e:
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'Please select bus first.')
        except ValueError:
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'No bus to delete.')

    def Delete_Line(self):
        try:
            n = self.LinelistWidget.selectedIndexes()[0].row()
            self.powergrid.delete_line(n)
            self.LinelistWidget.takeItem(n)
            self.num_line -= 1
        except IndexError as e:
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'Please select bus first.')
        except ValueError:
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'No bus to delete.')

    def Delete_Trans(self):
        try:
            n = self.TranslistWidget.selectedIndexes()[0].row()
            self.powergrid.delete_transformer(n)
            self.TranslistWidget.takeItem(n)
            self.num_Trans -= 1
        except IndexError as e:
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'Please select bus first.')
        except ValueError:
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'No bus to delete.')

    def Save_button(self):
        pg = self.powergrid
        fname = QtWidgets.QFileDialog.getSaveFileName(MainWindow, 'Save file', './')
        if fname[0]:
            try:
                f = open(fname[0], 'w')

                line1 = str(pg.numBus) + ',' + str(pg.numBus1) + ',' + str(pg.numBus2) + ',' \
                        + str(pg.numLine) + ',' + str(pg.numTransformer) + ',' \
                        + str(pg.V_initial) + ',' + str(pg.char_matrix[0][5])
                f.write(line1 + '\n')
                f.write('\n')

                for bus in pg.char_matrix[1:]:
                    line = str(bus[0]) + ',' + str(bus[3]) + ',' + str(bus[4]) + ',' + str(bus[5]) + ',' + str(bus[6])
                    f.write(line + '\n')

                f.write('\n')

                for Line in pg.line_list:
                    line = str(Line[0]) + ';' + str(Line[1].get_paras())
                    f.write(line + '\n')

                f.write('\n')

                for transformer in pg.transformer_list:
                    line = str(transformer[0]) + ';' + str(transformer[1].get_paras())
                    f.write(line + '\n')

                f.close()
            except FileNotFoundError as e:
                QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'File not found.')

    def Load_button(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file', './')
        if fname[0]:
            try:
                # 初始化窗口和PowerGrid
                self.powergrid = PowerGrid()
                self.clear()

                f = open(fname[0], 'r')

                line = f.readline().split(',')
                num, num1, num2, numLine, numTransformer = map(int, line[:5])
                isVset = bool(line[5])
                V = float(line[6])
                if not isVset:
                    f.close()
                else:
                    self.BuslistWidget.addItem("Bus" + str(self.num_bus) + '  Vθ')
                    # self.TextBus.append("Bus" + str(self.num_bus) + '  Vθ\n')
                    self.lineEdit.setText(str(V))
                    self.num_bus += 1
                    self.powergrid.set_V(V, 0.0)

                    f.readline()

                    for i in range(num-1):
                        line = f.readline().split(',')
                        P, Q, V, k = map(float, line[1:])
                        if line[0] == '1':
                            self.powergrid.add_bus(P=P, Q=Q, k=k, busType=1)
                            self.BuslistWidget.addItem("Bus" + str(self.num_bus) + '  PQ')
                        if line[0] == '2':
                            self.powergrid.add_bus(P=P, V=V, k=k, busType=2)
                            self.BuslistWidget.addItem("Bus" + str(self.num_bus) + '  PV')

                        self.num_bus += 1

                    f.readline()

                    for i in range(numLine):
                        line = f.readline().split(';')
                        location = tuple(map(int, tuple(line[0].strip('(').strip(')').split(','))))
                        paras = tuple(map(float, tuple(line[1].strip('(').strip('\n').strip(')').split(','))))
                        self.powergrid.add_line(location, Line(paraKnown=True, paras=paras))
                        self.LinelistWidget.addItem("Line" + str(self.num_line) + "  " + str(location))
                        self.num_line += 1

                    f.readline()

                    for i in range(numTransformer):
                        line = f.readline().split(';')
                        location = tuple(map(int, tuple(line[0].strip('(').strip(')').split(','))))
                        paras = tuple(map(float, tuple(line[1].strip('(').strip('\n').strip(')').split(','))))
                        self.powergrid.add_transformer(location, Transformer(paraKnown=True, paras=paras))
                        self.TranslistWidget.addItem("Transformer" + str(self.num_Trans) + "  " + str(location))
                        self.num_Trans += 1

                    f.close()
                    # self.powergrid.print_grid()
            except FileNotFoundError as e:
                QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'File not found.')

            except (ValueError, IndexError) as e:
                QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'Wrong file format.')

    def Calculate_button(self):
        try:
            self.powergrid.get_adm_matrix()
            self.powergrid.calculate_V(100, 1e-6)
            # self.powergrid.print_grid()

            # self.print2file()
            Dialog = QtWidgets.QDialog()
            ui = Calculate.Ui_Calculate()
            ui.setupUi(Dialog)
            Dialog.show()

            Ymatrix = self.powergrid.adm_matrix
            n = self.num_bus
            c_matrix = self.powergrid.result

            ui.AdmittanceMatrix.setColumnCount(n)
            ui.AdmittanceMatrix.setRowCount(n)
            ui.AdmittanceMatrix.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            ui.AdmittanceMatrix.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            for row in range(n):
                for column in range(n):
                    re = round(Ymatrix[row][column].real, 3)
                    im = round(Ymatrix[row][column].imag, 3)
                    item = QtWidgets.QTableWidgetItem(str(re) + '+' + str(im) + 'j')
                    # 设置每个位置的文本
                    ui.AdmittanceMatrix.setItem(row, column, item)

            ui.BusVoltage.setColumnCount(n)  # 这里需要输入Bus的数量
            ui.BusVoltage.setRowCount(3)
            alist = []
            for column in range(n):
                alist.append('V' + str(column))

            # ui.BusVoltage.setHorizontalHeaderLabels(alist)  # 这里更改为V0到Vn
            # v_header = [QtWidgets.QTableWidgetItem('e'), QtWidgets.QTableWidgetItem('f')]
            # ui.BusVoltage.setVerticalHeaderLabels(['e', 'f'])
            # ui.BusVoltage.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            # ui.BusVoltage.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            #
            # for row in range(n):
            #     item_e = QtWidgets.QTableWidgetItem(str(round(c_matrix[row][1], 3)))
            #     item_f = QtWidgets.QTableWidgetItem(str(round(c_matrix[row][2], 3)))
            #     ui.BusVoltage.setItem(0, row, item_e)
            #     ui.BusVoltage.setItem(1, row, item_f)

            ui.BusVoltage.setHorizontalHeaderLabels(alist)  # 这里更改为V0到Vn
            ui.BusVoltage.setVerticalHeaderLabels(['e', 'f', '|V|'])
            ui.BusVoltage.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            ui.BusVoltage.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            for row in range(n):
                item_e = QtWidgets.QTableWidgetItem(str(round(c_matrix[row][1], 5)))
                item_f = QtWidgets.QTableWidgetItem(str(round(c_matrix[row][2], 5)))
                v = sqrt(c_matrix[row][1] ** 2 + c_matrix[row][2] ** 2)
                item_v = QtWidgets.QTableWidgetItem(str(round(v, 5)))
                ui.BusVoltage.setItem(0, row, item_e)
                ui.BusVoltage.setItem(1, row, item_f)
                ui.BusVoltage.setItem(2, row, item_v)

            LineList = []
            i = 0
            for row in self.powergrid.loss_list:
                i += 1
                k, l = row[0]
                LineList.append(str(k) + ' to ' + str(l))
            ui.LineLoss.setRowCount(1)
            ui.LineLoss.setColumnCount(i)
            ui.LineLoss.setHorizontalHeaderLabels(LineList)
            n = 0
            for row in self.powergrid.loss_list:
                loss = QtWidgets.QTableWidgetItem(str(round(row[1].real, 3)) + '\n+j' + str(round(row[1].imag, 3)))
                ui.LineLoss.setItem(0, n, loss)
                n += 1
            ui.LineLoss.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            ui.LineLoss.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            rsp = Dialog.exec_()
            if rsp == QtWidgets.QDialog.Accepted:
                self.print2file()

        except (ValueError, IndexError) as e:
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'Invalid input.')
        except np.linalg.LinAlgError as e:
            QtWidgets.QMessageBox.critical(MainWindow, 'Error', e.args[0])
            # print(traceback.print_exc())

    def print2file(self):
        pg = self.powergrid
        fname = QtWidgets.QFileDialog.getSaveFileName(MainWindow, 'Save file', './')
        if fname[0]:
            try:
                f = open(fname[0] + '.txt', 'w')

                f.write('Grid information: \n')

                tb = pt.PrettyTable()
                tb.field_names = ['bus #', 'PQ bus #', 'PV bus #', 'line #', 'transformer #']
                tb.add_row([pg.numBus, pg.numBus1, pg.numBus2, pg.numLine, pg.numTransformer])

                f.write(str(tb) + '\n')
                f.write('Bus information: \n')

                tb = pt.PrettyTable()
                tb.field_names = ['bus type', 'P', 'Q', 'V', 'relative voltage level']
                for bus in pg.char_matrix:
                    if bus[0] == 0:
                        tb.add_row(['VΘ'] + bus[3:])
                    elif bus[0] == 1:
                        tb.add_row(['PQ'] + bus[3:])
                    elif bus[0] == 2:
                        tb.add_row(['PV'] + bus[3:])

                f.write(str(tb) + '\n')
                f.write('Line information: \n')

                tb = pt.PrettyTable()
                tb.field_names = ['location', 'R', 'X', 'B', 'G']
                for line in pg.line_list:
                    tb.add_row([str(line[0])] + list(line[1].get_paras()))

                f.write(str(tb) + '\n')
                f.write('Transformer information: \n')

                tb = pt.PrettyTable()
                tb.field_names = ['location', 'R', 'X', 'B', 'G']
                for transformer in pg.transformer_list:
                    tb.add_row([str(transformer[0])] + list(transformer[1].get_paras()))

                f.write(str(tb) + '\n')
                f.write('Admittance matrix: \n')

                Ymatrix = np.array(pg.adm_matrix)
                G_matrix = Ymatrix.real.tolist()
                B_matrix = Ymatrix.imag.tolist()

                tb = pt.PrettyTable()
                tb.title = 'G matrix'
                tb.field_names = ['bus' + str(i) for i in range(pg.numBus)]
                for row in G_matrix:
                    tb.add_row([round(x, 3) for x in row])

                f.write(str(tb) + '\n')

                tb = pt.PrettyTable()
                tb.title = 'B matrix'
                tb.field_names = ['bus' + str(i) for i in range(pg.numBus)]
                for row in B_matrix:
                    tb.add_row([round(x, 3) for x in row])

                f.write(str(tb) + '\n')
                f.write('Voltage on each buses: \n')

                tb = pt.PrettyTable()
                tb.field_names = ['e', 'f']
                for bus in pg.result:
                    tb.add_row(bus[1:3])

                f.write(str(tb) + '\n')
                f.write('Power loss on each devices: \n')

                tb = pt.PrettyTable()
                tb.field_names = ['device location', 'Real', 'Image']
                for loss in pg.loss_list:
                    tb.add_row([loss[0], round(loss[1].real, 3), round(loss[1].imag, 3)])

                f.write(str(tb) + '\n')
                f.write('Power flow on each devices: \n')

                tb = pt.PrettyTable()
                tb.field_names = ['device location' , 'Real', 'Image']
                for flow in pg.flow_list:
                    tb.add_row([flow[0], round(flow[1].real, 3), round(flow[1].imag, 3)])

                f.write(str(tb) + '\n')


                f.close()
            except Exception as e:
                print(traceback.print_exc())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Power Analysis"))
        self.Title.setText(_translate("MainWindow", "Power Flow Analysis"))
        self.busBox.setTitle(_translate("MainWindow", "Bus"))
        self.AddBus.setText(_translate("MainWindow", "Add"))
        self.DeleteBus.setText(_translate("MainWindow", "Delete"))
        self.transformerBox.setTitle(_translate("MainWindow", "Transformer"))
        self.AddTransformer.setText(_translate("MainWindow", "Add"))
        self.DeleteTransformer.setText(_translate("MainWindow", "Delete"))
        self.lineBox.setTitle(_translate("MainWindow", "Line"))
        self.AddLine.setText(_translate("MainWindow", "Add"))
        self.DeleteLine.setText(_translate("MainWindow", "Delete"))
        self.Load.setText(_translate("MainWindow", "Load Design"))
        self.Save.setText(_translate("MainWindow", "Save Design"))
        self.toolBox.setTitle(_translate("MainWindow", "Tool"))
        self.label.setText(_translate("MainWindow", "V:"))
        self.SetVoltage.setText(_translate("MainWindow", "Set Voltage"))
        self.Calculate.setText(_translate("MainWindow", "Calculate"))
        self.ClearAll.setText(_translate("MainWindow", "Clear All"))
        self.BusModifyBtn.setText(_translate("MainWindow", "Modify"))
        self.TransModifyBtn.setText(_translate("MainWindow", "Modify"))
        self.LineModifyBtn.setText(_translate("MainWindow", "Modify"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
