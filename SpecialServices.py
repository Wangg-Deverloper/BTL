# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Spa_and_Extra_services.ui'
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
        self.lbl_SPECAIL_SERVICES = QtWidgets.QLabel(self.centralwidget)
        self.lbl_SPECAIL_SERVICES.setGeometry(QtCore.QRect(290, 120, 591, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_SPECAIL_SERVICES.setFont(font)
        self.lbl_SPECAIL_SERVICES.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_SPECAIL_SERVICES.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_SPECAIL_SERVICES.setObjectName("lbl_SPECAIL_SERVICES")
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
        self.lbl_hairSpa = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hairSpa.setGeometry(QtCore.QRect(90, 380, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hairSpa.setFont(font)
        self.lbl_hairSpa.setObjectName("lbl_hairSpa")
        self.lbl_bodySpa = QtWidgets.QLabel(self.centralwidget)
        self.lbl_bodySpa.setGeometry(QtCore.QRect(90, 460, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_bodySpa.setFont(font)
        self.lbl_bodySpa.setObjectName("lbl_bodySpa")
        self.lbl_hotWaterbath = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hotWaterbath.setGeometry(QtCore.QRect(90, 540, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hotWaterbath.setFont(font)
        self.lbl_hotWaterbath.setObjectName("lbl_hotWaterbath")
        self.lbl_outdoorGym = QtWidgets.QLabel(self.centralwidget)
        self.lbl_outdoorGym.setGeometry(QtCore.QRect(90, 620, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_outdoorGym.setFont(font)
        self.lbl_outdoorGym.setObjectName("lbl_outdoorGym")
        self.lbl_indoorGym = QtWidgets.QLabel(self.centralwidget)
        self.lbl_indoorGym.setGeometry(QtCore.QRect(90, 700, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_indoorGym.setFont(font)
        self.lbl_indoorGym.setObjectName("lbl_indoorGym")
        self.txt_outdoorGym = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_outdoorGym.setGeometry(QtCore.QRect(310, 630, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txt_outdoorGym.setFont(font)
        self.txt_outdoorGym.setObjectName("txt_outdoorGym")
        self.txt_hotWaterbath = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_hotWaterbath.setGeometry(QtCore.QRect(310, 550, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txt_hotWaterbath.setFont(font)
        self.txt_hotWaterbath.setObjectName("txt_hotWaterbath")
        self.txt_bodySpa = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_bodySpa.setGeometry(QtCore.QRect(310, 470, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txt_bodySpa.setFont(font)
        self.txt_bodySpa.setObjectName("txt_bodySpa")
        self.txt_hairSpa = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_hairSpa.setGeometry(QtCore.QRect(310, 390, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txt_hairSpa.setFont(font)
        self.txt_hairSpa.setObjectName("txt_hairSpa")
        self.txt_indoorGym = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_indoorGym.setGeometry(QtCore.QRect(310, 710, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txt_indoorGym.setFont(font)
        self.txt_indoorGym.setObjectName("txt_indoorGym")
        self.lbl_NumPeople = QtWidgets.QLabel(self.centralwidget)
        self.lbl_NumPeople.setGeometry(QtCore.QRect(310, 300, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_NumPeople.setFont(font)
        self.lbl_NumPeople.setObjectName("lbl_NumPeople")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_RoomNum.setText(_translate("MainWindow", "Room Number"))
        self.lbl_SPECAIL_SERVICES.setText(_translate("MainWindow", "*****Special Services*****"))
        self.btn_SAVE.setText(_translate("MainWindow", "SAVE"))
        self.lbl_hairSpa.setText(_translate("MainWindow", "Hair Spa--->Rs1.0k"))
        self.lbl_bodySpa.setText(_translate("MainWindow", "Body Spa--->Rs2.2k"))
        self.lbl_hotWaterbath.setText(_translate("MainWindow", "Hot Waterbath--->Rs1.0k"))
        self.lbl_outdoorGym.setText(_translate("MainWindow", "Outdoor Gym--->Rs700"))
        self.lbl_indoorGym.setText(_translate("MainWindow", "Indoor Gym--->Rs680"))
        self.lbl_NumPeople.setText(_translate("MainWindow", "No. of people"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
