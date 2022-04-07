# from untitled import *
# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# sys.exit(app.exec_())

import sqlite3
import tkinter
from tkinter import *
from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


Form, Window = uic.loadUiType("untitled.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

global db
global sql

db = sqlite3.connect('person.db')
sql = db.cursor()


def on_c():
    print("1")


# def check_button():
#     sql.execute("""CREATE TABLE IF NOT EXISTS persons (
#         login TEXT,
#         password TEXT
#     )""")
#     db.commit()
#
#     sql.execute(f"SELECT login FROM persons WHERE login = ?", [login_user.get()])
#     if sql.fetchone() is None:
#         sql.execute(f"INSERT INTO persons VALUES('{login_user.get()}', '{password_user.get()}')")
#         db.commit()
#         print("Зарегистрировано")
#     else:
#         print("Запись уже есть")




form.registration_window.clicked.connect(on_c)

app.exec()

