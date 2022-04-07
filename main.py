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
Form2, Window2 = uic.loadUiType("untitled_new_task.ui")
Form3, Window3 = uic.loadUiType("untitled_reg.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

app2 = QApplication([])
window2 = Window2()
form2 = Form2()
form2.setupUi(window2)

app3 = QApplication([])
window3 = Window3()
form3 = Form3()
form3.setupUi(window3)

# global db
# global sql
#
# db = sqlite3.connect('person.db')
# sql = db.cursor()


def new_task_open():
    print("666")
    form.money.setText("5")
    window2.show()


def reg_open():
    window3.show()

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


form.registration_window.clicked.connect(reg_open)
form.pushButton.clicked.connect(new_task_open)



app.exec()

