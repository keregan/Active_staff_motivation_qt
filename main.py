# from untitled import *
# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# sys.exit(app.exec_())
import hashlib
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


def call_number(value):
    return hashlib.md5(value.encode()).hexdigest()


with sqlite3.connect("User_db.db") as user_db:
    cursor_db = user_db.cursor()

    cursor_db.executescript("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_login VARCHAR(30) NOT NULL,
        user_password VARCHAR(30) NOT NULL,
        first_name VARCHAR(30) NOT NULL,
        second_name VARCHAR(30) NOT NULL,
        patronymic VARCHAR(30) NOT NULL,
        position VARCHAR(100) NOT NULL,
        ball INTEGER NOT NULL DEFAULT 0
    )""")


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

    # test = form_main.calendarWidget.selectedDate().addDays(+pas_day)
    # print(test)


def reg_one_open():
    window_reg_one.show()


def reg_close():

    user_login = form_reg.user_login.text()
    user_password = form_reg.user_password.text()

    if not user_login or not user_password:
        form_reg.response_to_user.setText("Заполните все поля")
    else:
        try:
            user_db_login = sqlite3.connect("User_db.db")
            cursor_db_login = user_db_login.cursor()

            user_db_login.create_function("md5", 1, call_number)

            cursor_db_login.execute("SELECT user_login FROM users WHERE user_login = ?", [user_login])
            user_db_login.commit()
            c_log = cursor_db_login.fetchone()
            if c_log is None:
                form_reg.response_to_user.setText("Такого логина нету, зарегистрируйтесь")
            else:
                cursor_db_login.execute("SELECT user_password FROM users WHERE user_login = ? "
                                        "AND user_password = md5(?)", [user_login, user_password])
                user_db_login.commit()
                c_pas = cursor_db_login.fetchone()
                if c_pas is None:
                    form_reg.response_to_user.setText("Пароль не верный")
                else:
                    user_login = form_reg.user_login.setText("")
                    user_password = form_reg.user_password.setText("")
                    window_reg.close()
        except sqlite3.Error as err:
            form_reg.response_to_user.setText(err)
        finally:
            cursor_db_login.close()
            user_db_login.close()


def reg_one_close():
    user_login = form_reg_one.user_login.text()
    user_password = form_reg_one.user_password.text()
    first_name = form_reg_one.first_name.text()
    second_name = form_reg_one.second_name.text()
    patronymic = form_reg_one.patronymic.text()
    position = form_reg_one.position.text()

    if not user_login or not user_password or not first_name or not second_name or not patronymic or not position:
        if not user_login:
            form_reg_one.Error.setText("Введите новый логин")
        else:
            form_reg_one.Error.setText("Заполните все поля")
    else:
        try:
            user_db_reg = sqlite3.connect("User_db.db")
            cursor_db_reg = user_db_reg.cursor()

            cursor_db_reg.execute("SELECT user_login FROM users WHERE user_login = ?", [user_login])
            user_db_reg.commit()
            c_log = cursor_db_reg.fetchone()
            if c_log is None:
                user_db_reg.create_function("md5", 1, call_number)
                u_db = [user_login, user_password, first_name, second_name, patronymic, position]
                cursor_db_reg.execute("INSERT INTO users(user_login, user_password, first_name, second_name, "
                                      "patronymic, position) VALUES(?, md5(?), ?, ?, ?, ?)", u_db)
                user_db_reg.commit()

                form_reg_one.user_login.setText("")
                form_reg_one.user_password.setText("")
                form_reg_one.first_name.setText("")
                form_reg_one.second_name.setText("")
                form_reg_one.patronymic.setText("")
                form_reg_one.position.setText("")
                app_reg_one.closeAllWindows()
            else:
                form_reg_one.user_login.setText("")
                reg_one_close()

        except sqlite3.Error as err:
            form_reg_one.Error.setText(err)
        finally:
            cursor_db_reg.close()
            user_db_reg.close()


# def log_in():
#     user_login = 1
#     user_password = 1
#
#     try:
#         user_db_login = sqlite3.connect("User_db.db")
#         cursor_db_login = user_db_login.cursor()
#
#         user_db_login.create_function("md5", 1, call_number)
#
#         cursor_db_login.execute("SELECT login FROM users WHERE login = ?", [user_login])
#         if cursor_db_login.fetchone() is NONE:
#             print("такого логина нету")
#         else:
#             cursor_db_login.execute("SELECT password FROM users WHERE login = ? AND"
#                                     " password = md5(?)", [user_login, user_password])
#             if cursor_db_login.fetchone() is NONE:
#                 print("Пароль не верный")
#             else:
#                 print("Пароль верный")
#     except sqlite3.Error as e:
#         print("Error", e)
#     finally:
#         cursor_db_login.close()
#         user_db_login.close()


# form_main.pushButton_2.clicked.connect(starter)
form_main.registration_window.clicked.connect(reg_open)
# form_main.pushButton.clicked.connect(new_task_open)
# form_new_task.pushButton.clicked.connect(create_new_task)
form_reg.register_button.clicked.connect(reg_one_open)
form_reg.login_button.clicked.connect(reg_close)
form_reg_one.login_button.clicked.connect(reg_one_close)

app_main.exec()

