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

Form_main, Window_main = uic.loadUiType("untitled.ui")
Form_new_task, Window_new_task = uic.loadUiType("untitled_new_task.ui")
Form_reg, Window_reg = uic.loadUiType("untitled_reg.ui")
Form_reg_one, Window_reg_one = uic.loadUiType("untitled_reg_one.ui")

app_main = QApplication([])
window_main = Window_main()
form_main = Form_main()
form_main.setupUi(window_main)
window_main.show()

app_new_task = QApplication([])
window_new_task = Window_new_task()
form_new_task = Form_new_task()
form_new_task.setupUi(window_new_task)
# window_new_task.show()

app_reg = QApplication([])
window_reg = Window_reg()
form_reg = Form_reg()
form_reg.setupUi(window_reg)
# window_reg.show()

app_reg_one = QApplication([])
window_reg_one = Window_reg_one()
form_reg_one = Form_reg_one()
form_reg_one.setupUi(window_reg_one)
# window_reg_one.show()

# global db
# global sql

# db = sqlite3.connect('person.db')
# sql = db.cursor()


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


def reg_one_open():
    window_reg_one.show()


def reg_close():

    window_reg.close()


def reg_one_close():

    app_reg_one.closeAllWindows()


form_main.pushButton_2.clicked.connect(starter)
form_main.registration_window.clicked.connect(reg_open)
form_main.pushButton.clicked.connect(new_task_open)
form_new_task.pushButton.clicked.connect(create_new_task)
form_reg.register_button.clicked.connect(reg_one_open)
form_reg.login_button.clicked.connect(reg_close)
form_reg_one.login_button.clicked.connect(reg_one_close)

app_main.exec()

