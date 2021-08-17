# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\PycharmProjects\pythonProject\button2_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 491)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/로고_아이콘.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 280, 287, 41))
        self.pushButton.setStyleSheet('QPushButton {background-color: #98bfe0; color: white; border-radius: 25px;}')
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 341, 471))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/background/bg.png"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 110, 271, 121))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 330, 287, 41))
        self.pushButton_2.setStyleSheet('QPushButton {background-color: #98bfe0; color: white; border-radius: 25px;}')
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 380, 287, 41))
        self.pushButton_3.setStyleSheet('QPushButton {background-color: #98bfe0; color: white; border-radius: 25px;}')
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.collect_1)
        self.pushButton_2.clicked.connect(Dialog.collect_2)
        self.pushButton_3.clicked.connect(Dialog.collect_3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "데이터 수집하기"))
        self.pushButton.setText(_translate("Dialog", "수집 시작하기"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">원활한 데이터 수집을 위해</p><p align=\"center\">크롬 창 영역을 </p><p align=\"center\">침범하지 말아주세요 :)</p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "수집 완료하기"))
        self.pushButton_3.setText(_translate("Dialog", "수집한 데이터 정리하기"))
import testResource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
