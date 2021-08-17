# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\PycharmProjects\pythonProject\button1_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/로고_아이콘.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 281, 71))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('QPushButton {background-color: #e3b94d; color: white; border-radius: 25px;}')
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(100, 230, 31, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setText("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.txt_1 = QtWidgets.QLabel(Dialog)
        self.txt_1.setGeometry(QtCore.QRect(70, 110, 311, 101))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_1.setFont(font)
        self.txt_1.setObjectName("txt_1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 220, 231, 61))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Light")
        font.setPointSize(10)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 361, 491))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/background/bg.png"))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.pushButton.raise_()
        self.commandLinkButton.raise_()
        self.txt_1.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "사용 전 필독사항"))
        self.pushButton.setText(_translate("Dialog", "설치 완료 !"))
        self.txt_1.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">프로그램 실행을 위해 </p><p align=\"center\">Chrome Driver 설치가 필요합니다.</p></body></html>"))
        self.label.setText('<a href="https://beaded-jaborosa-fdf.notion.site/Chrome-Driver-3e707acbdea44cd28af991708097e938">Chrome Driver 설치 가이드</a>')
import testResource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
