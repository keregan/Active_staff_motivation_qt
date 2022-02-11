# from untitled import *
# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# sys.exit(app.exec_())

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("untitled.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def on_c():
    print("1")


form.registration_window.clicked.connect(on_c)

app.exec()

