import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from button1_ui import Ui_Dialog
from button2_ui import Ui_Dialog2

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


class mainWindow(QMainWindow, myUIClass):
    def __init__(self):
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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = mainWindow()
    myWindow.show()
    app.exec_()