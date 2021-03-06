import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from button1_ui import Ui_Dialog
from button2_ui import Ui_Dialog2
from button3_ui import Ui_Dialog3
import web_crawling as wc
import html_parsing as hp
import data_visualization as dv


myUIClass = uic.loadUiType("main.ui")[0]

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class MyDialog2(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)

    def collect_1(self):
        wc.crop_func()

    def collect_3(self):
        hp.get_files()

class MyDialog3(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self)
        dv.get_files()


    def result_1(self):
        dv.yesterday_vacc()

    def result_2(self):
        dv.acc_vacc()

    def result_3(self):
        dv.hosp_acc()

    def result_4(self):
        dv.acc_trend()

    def result_5(self):
        dv.vacc_time()

    def result_6(self):
        dv.time_hosp()

    def result_7(self):
        dv.show_hosps()

class mainWindow(QMainWindow, myUIClass):
    def __init__(self):
        dv.get_files()
        super().__init__()
        self.setupUi(self)
        self.ui = uic.loadUi("main.ui", self)
        self.pushButton_1.setStyleSheet('QPushButton {background-color: #e3b94d; color: white; border-radius: 25px;}')
        self.pushButton_2.setStyleSheet('QPushButton {background-color: #98bfe0; color: white; border-radius: 25px;}')
        self.pushButton_3.setStyleSheet('QPushButton {background-color: #4a94b0; color: white; border-radius: 25px;}')

    def must(self):
        self.myDialog = MyDialog()
        self.myDialog.show()

    def collect(self):
        self.myDialog2 = MyDialog2()
        self.myDialog2.show()

    def result(self):
        self.myDialog3 = MyDialog3()
        self.myDialog3.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = mainWindow()
    myWindow.show()
    app.exec_()