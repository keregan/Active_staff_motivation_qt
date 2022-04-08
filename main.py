# from untitled import *
# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# sys.exit(app.exec_())
import datetime
import time
import sqlite3
import tkinter
from tkinter import *
from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("untitled.ui")
Form2, Window2 = uic.loadUiType("untitled_new_task.ui")
Form3, Window3 = uic.loadUiType("untitled_reg.ui")

app_main = QApplication([])
window_main = Window()
form_main = Form()
form_main.setupUi(window_main)
window_main.show()

app_new_task = QApplication([])
window_new_task = Window2()
form_new_task = Form2()
form_new_task.setupUi(window_new_task)

app_reg = QApplication([])
window_reg = Window3()
form_reg = Form3()
form_reg.setupUi(window_reg)

# global db
# global sql

# db = sqlite3.connect('person.db')
# sql = db.cursor()


# def pre_start():
#     one = form_main.label_31.text()
#     print(one)
#     ball = 11 + int(one)
#     print(ball)
#     form_main.user_data.setText(ball)
#     print("1qq")

def starter():
    to_day = datetime.date.today()
    form_main.dateEdit.setMinimumDate(to_day)


def new_task_open():
    # print("66")
    # form.money.setText("5")
    window_new_task.show()

    to_day = datetime.date.today()
    form_new_task.dateEdit.setMinimumDate(to_day)


def reg_open():
    window_reg.show()

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


# def new_task_close():
#     app2.exec()


def reg_close():
    app_reg.closeAllWindows()


def create_new_task():
    line = form_new_task.lineEdit.text()
    form_main.lineEdit.setText(line)
    form_new_task.lineEdit.setText("")

    status = form_new_task.comboBox.currentText()
    form_main.label_6.setText(status)

    descr = form_new_task.textEdit.toPlainText()
    form_main.textEdit.setPlainText(descr)
    form_new_task.textEdit.setPlainText("")

    ball_one = form_new_task.spinBox.text()
    form_main.label_31.setText(ball_one)

    grt = form_new_task.lineEdit_2.text()
    form_main.label_17.setText(grt)

    data_task = form_new_task.dateEdit.date()
    to_day = form_main.dateEdit.date()
    pas_day = to_day.daysTo(data_task)
    form_main.TextLabel.setText(str(pas_day))

    test = form_main.calendarWidget.selectedDate().addDays(+pas_day)
    print(test)

    # tt = too_day - data_task
    # print(too_day)
    # past_day = data_task - to_day
    # print(past_day)


form_main.pushButton_2.clicked.connect(starter)
form_main.registration_window.clicked.connect(reg_open)
form_main.pushButton.clicked.connect(new_task_open)
form_new_task.pushButton.clicked.connect(create_new_task)
form_reg.pushButton.clicked.connect(reg_close)

app_main.exec()

