from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import Window , DataCus, Restaurant, Laundry, Game, Bar, Amusement, CarRental, SpecialServices


ui =''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
def mainUi():
    global ui
    ui = Window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_AddCus.clicked.connect(dataCus)
    ui.btn_Restaurant.clicked.connect(restaurant)
    ui.btn_Laundry.clicked.connect(laundry)
    ui.btn_Game.clicked.connect(game)
    ui.btn_Bar.clicked.connect(bar)
    ui.btn_Amusement.clicked.connect(amusementActivity)
    ui.btn_CarRental.clicked.connect(carRental)
    ui.btn_Spa.clicked.connect(specialServices)
    # ui.btn_Find.clicked.connect(tracuu)
    ui.btn_Exit.clicked.connect(EXIT)
    MainWindow.show()

def dataCus():
    global ui
    ui = DataCus.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_SAVE.clicked.connect(mainUi)
    MainWindow.show()

def restaurant():
    global ui
    ui = Restaurant.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_SAVE.clicked.connect(mainUi)
    MainWindow.show()

def laundry():
    global ui
    ui = Laundry.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_SAVE.clicked.connect(mainUi)
    MainWindow.show()

def game():
    global ui
    ui = Game.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_SAVE.clicked.connect(mainUi)
    MainWindow.show()

def bar():
    global ui
    ui = Bar.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_SAVE.clicked.connect(mainUi)
    MainWindow.show()

def amusementActivity():
    global ui
    ui = Amusement.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_SAVE.clicked.connect(mainUi)
    MainWindow.show()

def carRental():
    global ui
    ui = CarRental.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_SAVE.clicked.connect(mainUi)
    MainWindow.show()

def specialServices():
    global ui
    ui = SpecialServices.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_SAVE.clicked.connect(mainUi)
    MainWindow.show()

# def tracuu():
#     global ui
#     ui = TraCuu.Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     ui.btn_Find.clicked.connect(mainUi)
#     MainWindow.show()
def EXIT():
    exit()
    return()

mainUi()
sys.exit(app.exec_())

