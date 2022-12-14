# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1175, 890)
        MainWindow.setMinimumSize(QtCore.QSize(1175, 890))
        MainWindow.setMaximumSize(QtCore.QSize(1175, 890))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_RoomNum = QtWidgets.QLabel(self.centralwidget)
        self.lbl_RoomNum.setGeometry(QtCore.QRect(90, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_RoomNum.setFont(font)
        self.lbl_RoomNum.setObjectName("lbl_RoomNum")
        self.lbl_GAME = QtWidgets.QLabel(self.centralwidget)
        self.lbl_GAME.setGeometry(QtCore.QRect(300, 120, 651, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_GAME.setFont(font)
        self.lbl_GAME.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_GAME.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_GAME.setObjectName("lbl_GAME")
        self.txt_RoomNum = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_RoomNum.setGeometry(QtCore.QRect(230, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txt_RoomNum.setFont(font)
        self.txt_RoomNum.setObjectName("txt_RoomNum")
        self.btn_SAVE = QtWidgets.QPushButton(self.centralwidget)
        self.btn_SAVE.setGeometry(QtCore.QRect(440, 780, 301, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_SAVE.setFont(font)
        self.btn_SAVE.setObjectName("btn_SAVE")
        self.lbl_TableTennis = QtWidgets.QLabel(self.centralwidget)
        self.lbl_TableTennis.setGeometry(QtCore.QRect(90, 380, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_TableTennis.setFont(font)
        self.lbl_TableTennis.setObjectName("lbl_TableTennis")
        self.lbl_Bowling = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Bowling.setGeometry(QtCore.QRect(90, 460, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_Bowling.setFont(font)
        self.lbl_Bowling.setObjectName("lbl_Bowling")
        self.lbl_Snooker = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Snooker.setGeometry(QtCore.QRect(90, 540, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_Snooker.setFont(font)
        self.lbl_Snooker.setObjectName("lbl_Snooker")
        self.lbl_VideoGames = QtWidgets.QLabel(self.centralwidget)
        self.lbl_VideoGames.setGeometry(QtCore.QRect(90, 620, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_VideoGames.setFont(font)
        self.lbl_VideoGames.setObjectName("lbl_VideoGames")
        self.lbl_Pool = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Pool.setGeometry(QtCore.QRect(90, 700, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_Pool.setFont(font)
        self.lbl_Pool.setObjectName("lbl_Pool")
        self.txt_VideoGames = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_VideoGames.setGeometry(QtCore.QRect(350, 630, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txt_VideoGames.setFont(font)
        self.txt_VideoGames.setObjectName("txt_VideoGames")
        self.txt_Snooker = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_Snooker.setGeometry(QtCore.QRect(350, 550, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txt_Snooker.setFont(font)
        self.txt_Snooker.setObjectName("txt_Snooker")
        self.txt_Bowling = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_Bowling.setGeometry(QtCore.QRect(350, 470, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txt_Bowling.setFont(font)
        self.txt_Bowling.setObjectName("txt_Bowling")
        self.txt_TableTennis = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_TableTennis.setGeometry(QtCore.QRect(350, 390, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txt_TableTennis.setFont(font)
        self.txt_TableTennis.setObjectName("txt_TableTennis")
        self.txt_Pool = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_Pool.setGeometry(QtCore.QRect(350, 710, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txt_Pool.setFont(font)
        self.txt_Pool.setObjectName("txt_Pool")
        self.lbl_NumHour = QtWidgets.QLabel(self.centralwidget)
        self.lbl_NumHour.setGeometry(QtCore.QRect(360, 300, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_NumHour.setFont(font)
        self.lbl_NumHour.setObjectName("lbl_NumHour")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_RoomNum.setText(_translate("MainWindow", "Room Number"))
        self.lbl_GAME.setText(_translate("MainWindow", "******GAME MENU*******"))
        self.btn_SAVE.setText(_translate("MainWindow", "SAVE"))
        self.lbl_TableTennis.setText(_translate("MainWindow", "Table tennis----->Rs60"))
        self.lbl_Bowling.setText(_translate("MainWindow", "Bowling----->Rs80"))
        self.lbl_Snooker.setText(_translate("MainWindow", "Snooker--->Rs70"))
        self.lbl_VideoGames.setText(_translate("MainWindow", "Video games---->Rs90"))
        self.lbl_Pool.setText(_translate("MainWindow", "Pool--->Rs50"))
        self.lbl_NumHour.setText(_translate("MainWindow", "No. of hours"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
