# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\PycharmProjects\pythonProject\button3_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(461, 519)
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Light")
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/로고_아이콘.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 220, 191, 51))
        self.pushButton.setStyleSheet('QPushButton {background-color: #4a94b0; color: white; border-radius: 25px;}')
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 220, 191, 51))
        self.pushButton_2.setStyleSheet('QPushButton {background-color: #4a94b0; color: white; border-radius: 25px;}')
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 290, 191, 51))
        self.pushButton_3.setStyleSheet('QPushButton {background-color: #4a94b0; color: white; border-radius: 25px;}')
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 290, 191, 51))
        self.pushButton_4.setStyleSheet('QPushButton {background-color: #4a94b0; color: white; border-radius: 25px;}')
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 360, 191, 51))
        self.pushButton_5.setStyleSheet('QPushButton {background-color: #4a94b0; color: white; border-radius: 25px;}')
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 360, 191, 51))
        self.pushButton_6.setStyleSheet('QPushButton {background-color: #4a94b0; color: white; border-radius: 25px;}')
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(140, 430, 191, 51))
        self.pushButton_7.setStyleSheet('QPushButton {background-color: #4a94b0; color: white; border-radius: 25px;}')
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 90, 111, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/background/로고_연한거 (1).png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, -10, 431, 291))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/background/bg_2.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 0, 411, 601))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/background/bg-Light Gray.png"))
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.result_1)
        self.pushButton_2.clicked.connect(Dialog.result_2)
        self.pushButton_3.clicked.connect(Dialog.result_3)
        self.pushButton_4.clicked.connect(Dialog.result_4)
        self.pushButton_5.clicked.connect(Dialog.result_5)
        self.pushButton_6.clicked.connect(Dialog.result_6)
        self.pushButton_7.clicked.connect(Dialog.result_7)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "수집 결과 확인"))
        self.pushButton.setText(_translate("Dialog", "어제의 백신 발생량"))
        self.pushButton_2.setText(_translate("Dialog", "누적 백신 발생량"))
        self.pushButton_3.setText(_translate("Dialog", "병원별 누적 발생량"))
        self.pushButton_4.setText(_translate("Dialog", "일별 잔여백신 발생 추이"))
        self.pushButton_5.setText(_translate("Dialog", "백신 발생 시간대"))
        self.pushButton_6.setText(_translate("Dialog", "시간대별 병원"))
        self.pushButton_7.setText(_translate("Dialog", "근처 100개 병원 정보"))
import testResource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
