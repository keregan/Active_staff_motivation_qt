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

    cursor_db.executescript("""CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_login VARCHAR(30) NOT NULL,
        name_task_one VARCHAR(100) NOT NULL,
        status_task_one VARCHAR(30) NOT NULL,
        description_task_one VARCHAR(3000) NOT NULL,
        ball_one VARCHAR(30) NOT NULL,
        group_task_one VARCHAR(100) NOT NULL,
        lead_time_one DATA NOT NULL
    )""")


def main_form(user_login):
    try:
        user_db_main = sqlite3.connect("User_db.db")
        cursor_db_main = user_db_main.cursor()

        form_main.user_login.setText(user_login)
        cursor_db_main.execute("SELECT first_name FROM users WHERE user_login = ?", [user_login])
        user_db_main.commit()
        c_log1 = cursor_db_main.fetchone()
        cursor_db_main.execute("SELECT second_name FROM users WHERE user_login = ?", [user_login])
        user_db_main.commit()
        c_log2 = cursor_db_main.fetchone()
        cursor_db_main.execute("SELECT patronymic FROM users WHERE user_login = ?", [user_login])
        user_db_main.commit()
        c_log3 = cursor_db_main.fetchone()
        cursor_db_main.execute("SELECT position FROM users WHERE user_login = ?", [user_login])
        user_db_main.commit()
        c_log4 = cursor_db_main.fetchone()
        cursor_db_main.execute("SELECT ball FROM users WHERE user_login = ?", [user_login])
        user_db_main.commit()
        c_log5 = cursor_db_main.fetchone()
        form_main.user_data.setText(str(c_log1[0]) + " " + str(c_log2[0]) + " " + str(c_log3[0]))
        form_main.position.setText(str(c_log4[0]))
        form_main.ball.setText(str(c_log5[0]))
    except sqlite3.Error as err:
        form_main.user_data.setText(err)
    finally:
        cursor_db_main.close()
        user_db_main.close()


def starter():
    # to_day = datetime.date.today()
    # form_main.dateEdit.setMinimumDate(to_day)
    main_form("Alex_1")


def new_task_open():
    user_login = form_main.user_login.text()
    create_new_task(user_login)

    if not user_login or user_login == "Войдите в аккаунт":
        form_main.user_data.setText("Войдите в аккаунт")
    else:
        window_new_task.show()

    # to_day = datetime.date.today()
    # form_new_task.lead_time.setMinimumDate(to_day)


def create_new_task(user_login):
    name_task_one = form_new_task.name_task.text()
    status_task_one = form_new_task.status_task.currentText()
    description_task_one = form_new_task.description_task.toPlainText()
    ball_one = form_new_task.ball.text()
    group_task_one = form_new_task.group_task.text()
    lead_time_one = form_new_task.lead_time.date()

    if not name_task_one or not status_task_one or not description_task_one or not ball_one or not group_task_one or not lead_time_one:
        if not name_task_one:
            form_new_task.error_new_task.setText("Проверьте название или замените его")
        else:
            form_new_task.error_new_task.setText("Проверьте заполненость всех полей")
    else:
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            # cursor_db_task.execute("SELECT user_login FROM users WHERE user_login = ?", [user_login])
            # user_db_task.commit()
            #
            # c_log = cursor_db_task.fetchone()
            # if c_log is None:
            #     task_db = []
            #     cursor_db_task.execute("INSERT INTO users(user_login, user_password, first_name, second_name, "
            #                           "patronymic, position) VALUES(?, ?, ?, ?, ?, ?)", task_db)
            #     user_db_task.commit()
            #
            # else:

        except sqlite3.Error as err:
            form_new_task.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()

    # data_task = form_new_task.dateEdit.date()
    # to_day = form_main.dateEdit.date()
    # pas_day = to_day.daysTo(data_task)
    # form_main.TextLabel.setText(str(pas_day))

    # test = form_main.calendarWidget.selectedDate().addDays(+pas_day)
    # print(test)


def reg_open():
    window_reg.show()


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
                    # main_form(user_login)
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


form_main.pushButton_2.clicked.connect(starter)
form_main.registration_window.clicked.connect(reg_open)
form_main.pushButton.clicked.connect(new_task_open)
form_new_task.create_new_task.clicked.connect(create_new_task)
form_reg.register_button.clicked.connect(reg_one_open)
form_reg.login_button.clicked.connect(reg_close)
form_reg_one.login_button.clicked.connect(reg_one_close)

app_main.exec()

