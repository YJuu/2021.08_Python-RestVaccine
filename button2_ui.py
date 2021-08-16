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
        Dialog.resize(447, 529)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/로고_아이콘.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 287, 71))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('QPushButton {background-color: #98bfe0; color: white; border-radius: 25px;}')
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 341, 491))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/background/bg.png"))
        self.label_2.setObjectName("label_2")
        self.changetxt = QtWidgets.QLabel(Dialog)
        self.changetxt.setGeometry(QtCore.QRect(70, 400, 301, 61))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        font.setItalic(True)
        font.setUnderline(True)
        self.changetxt.setFont(font)
        self.changetxt.setObjectName("changetxt")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 110, 271, 121))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2.raise_()
        self.pushButton.raise_()
        self.changetxt.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "데이터 수집하기"))
        self.pushButton.setText(_translate("Dialog", "수집 시작하기"))
        self.changetxt.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">수집 완료 !</p><p align=\"center\"><span style=\" font-size:9pt; font-style:normal;\">창을 닫은 후 수집 결과를 확인해보세요. </span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">데이터 수집 중에는</p><p align=\"center\">컴퓨터 사용이</p><p align=\"center\">어렵습니다 :(</p></body></html>"))
import testResource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
