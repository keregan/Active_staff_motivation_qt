import hashlib
import datetime
import time
import sqlite3
import tkinter
from tkinter import *
from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


Form_main, Window_main = uic.loadUiType("untitled_2.ui")
Form_new_task, Window_new_task = uic.loadUiType("untitled_new_task.ui")
Form_upgrade_task, Window_upgrade_task = uic.loadUiType("untitled_upgrade_task.ui")
Form_reg, Window_reg = uic.loadUiType("untitled_reg.ui")
Form_reg_one, Window_reg_one = uic.loadUiType("untitled_reg_one.ui")
Form_task_old, Window_task_old = uic.loadUiType("untitled_task_old.ui")
Form_admin, Window_admin = uic.loadUiType("untitled_admin.ui")


app_main = QApplication([])
window_main = Window_main()
form_main = Form_main()
form_main.setupUi(window_main)
window_main.show()

app_admin = QApplication([])
window_admin = Window_admin()
form_admin = Form_admin()
form_admin.setupUi(window_admin)
# window_admin.show()


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

app_upgrade_task = QApplication([])
window_upgrade_task = Window_upgrade_task()
form_upgrade_task = Form_upgrade_task()
form_upgrade_task.setupUi(window_upgrade_task)
# window_upgrade_task.show()

app_task_old = QApplication([])
window_task_old = Window_task_old()
form_task_old = Form_task_old()
form_task_old.setupUi(window_task_old)
# window_task_old.show()


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
        ball INTEGER NOT NULL DEFAULT 0,
        auto_login VARCHAR(2) DEFAULT 0
    )""")

    cursor_db.executescript("""CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_login VARCHAR(30) NOT NULL,
        name_task_one VARCHAR(100) NOT NULL,
        status_task_one VARCHAR(30) NOT NULL,
        description_task_one VARCHAR(3000) NOT NULL,
        ball_one INTEGER NOT NULL,
        group_task_one VARCHAR(100) NOT NULL,
        lead_time_one DATA
    )""")

    cursor_db.executescript("""CREATE TABLE IF NOT EXISTS tasks_old(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_login VARCHAR(30) NOT NULL,
        name_task_one VARCHAR(100) NOT NULL,
        status_task_one VARCHAR(30) NOT NULL,
        description_task_one VARCHAR(3000) NOT NULL,
        ball_one INTEGER NOT NULL,
        group_task_one VARCHAR(100) NOT NULL,
        lead_time_one DATA
    )""")


def main_form():
    user_login = form_main.user_login.text()
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


def restarter():
    try:
        form_main.tasks_list.clear()
        user_db_task = sqlite3.connect("User_db.db")
        cursor_db_task = user_db_task.cursor()

        cursor_db_task.execute("SELECT user_login FROM users WHERE auto_login = 1")
        user_db_task.commit()
        user_login_1 = cursor_db_task.fetchone()
        user_login = str(user_login_1[0])
        form_main.user_login.setText(user_login)
        user_login = form_main.user_login.text()

        cursor_db_task.execute("SELECT user_login FROM users WHERE user_login = ?", [user_login])
        user_db_task.commit()
        none_login_task = cursor_db_task.fetchone()

        if none_login_task is None:
            form_main.user_data.setText("Войдите в аккаунт")
        else:
            cursor_db_task.execute(
                "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                "lead_time_one, id FROM tasks WHERE user_login = ?",
                [user_login])
            user_db_task.commit()
            rec = cursor_db_task.fetchall()

            for row in rec:
                ball_s = str(row[3])
                new_str_task = "ID: {0:25.10}".format(str(row[6])) + " " + "{0:.15}".format(row[0]) + "{0:300}".format(" ") + "{0:30.15}".format(row[1])

                # new_str_task = "ID: {0:.10} {1:.20} {2:.20} {3:.20}    Дата: ".format(str(row[6]), row[0], row[1], row[4]) + str(row[5])
                form_main.tasks_list.addItem(str(new_str_task))
            # year_task = int(s[0]) * 1000 + int(s[1]) * 100 + int(s[2]) * 10 + int(s[3])
            # month_task = int(s[5]) * 10 + int(s[6])
            # day_task = int(s[8]) * 10 + int(s[9])

            main_form()
    except sqlite3.Error as err:
        form_new_task.error_new_task.setText(err)
    finally:
        cursor_db_task.close()
        user_db_task.close()


def new_task_open():
    user_login = form_main.user_login.text()

    if not user_login or user_login == "Войдите в аккаунт":
        form_main.user_data.setText("Войдите в аккаунт")
    else:
        window_new_task.show()
        form_new_task.error_new_task.setText("")
        form_new_task.lead_time.setMinimumDate(datetime.date.today())


def create_new_task():
    name_task_one = form_new_task.name_task.text()
    status_task_one = form_new_task.status_task.currentText()
    description_task_one = form_new_task.description_task.toPlainText()
    ball_one = form_new_task.ball.text()
    group_task_one = form_new_task.group_task.text()
    lead_time_one = form_new_task.lead_time.date()
    lead_time_one_con = lead_time_one.toPyDate()
    user_login = form_main.user_login.text()

    if not name_task_one or not status_task_one or not description_task_one or not ball_one or not group_task_one or not lead_time_one:
        form_new_task.error_new_task.setText("Проверьте заполненость всех полей")
    else:
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            cursor_db_task.execute("SELECT user_login FROM tasks WHERE user_login = ? AND name_task_one = ?", [user_login, name_task_one])
            user_db_task.commit()
            none_name_task = cursor_db_task.fetchone()

            if none_name_task is None:
                task_db = [user_login, name_task_one, status_task_one, description_task_one, ball_one, group_task_one, lead_time_one_con]
                cursor_db_task.execute("INSERT INTO tasks(user_login, name_task_one, status_task_one, description_task_one, "
                                      "ball_one, group_task_one, lead_time_one ) VALUES(?, ?, ?, ?, ?, ?, ?)", task_db)
                user_db_task.commit()
                form_new_task.error_new_task.setText("Задача создана")
                restarter()
            else:
                form_new_task.error_new_task.setText("Запись с таким названием уже имеется")
        except sqlite3.Error as err:
            form_new_task.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def upgrade_new_task():
    id_task = form_upgrade_task.id_task.text()
    name_task_one = form_upgrade_task.name_task.text()
    status_task_one = form_upgrade_task.status_task.currentText()
    description_task_one = form_upgrade_task.description_task.toPlainText()
    ball_one = form_upgrade_task.ball.text()
    group_task_one = form_upgrade_task.group_task.text()
    lead_time_one = form_upgrade_task.lead_time.date()
    lead_time_one_con = lead_time_one.toPyDate()
    user_login = form_main.user_login.text()

    if not name_task_one or not status_task_one or not description_task_one or not ball_one or not group_task_one or not lead_time_one:
        form_new_task.error_upgrade_task.setText("Проверьте заполненость всех полей")
    else:
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            cursor_db_task.execute("SELECT user_login FROM tasks WHERE user_login = ? AND id = ?",
                                   [user_login, id_task])
            user_db_task.commit()

            task_db = [name_task_one, status_task_one, description_task_one, ball_one, group_task_one, lead_time_one_con, user_login, id_task]

            cursor_db_task.execute("UPDATE tasks SET name_task_one = ?, status_task_one = ?, description_task_one = ?,"
                                   " ball_one = ?, group_task_one = ?, lead_time_one = ? WHERE"
                                   " user_login = ? AND id = ?", task_db)
            user_db_task.commit()
            form_upgrade_task.error_new_task.setText("Успешно обновлено")
            restarter()
            window_upgrade_task.close()

            form_main.name_task.setText(name_task_one)
            form_main.status_task.setText(status_task_one)
            form_main.description_task.setText(description_task_one)
            form_main.ball_2.setText(str(ball_one))
            form_main.group_task.setText(group_task_one)
            form_main.date_task.setText(str(lead_time_one_con))
        except sqlite3.Error as err:
            form_upgrade_task.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def upgrade_task():
    user_login = form_main.user_login.text()
    id_task = form_main.number_task.text()

    if not user_login or user_login == "Войдите в аккаунт" or not id_task:
        if not user_login or user_login == "Войдите в аккаунт":
            form_main.user_data.setText("Войдите в аккаунт")
        else:
            form_main.error_task.setText("Выберите задачу")
    else:
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            cursor_db_task.execute("SELECT id FROM tasks WHERE user_login = ? AND id = ?", [user_login, id_task])
            user_db_task.commit()
            err_id = cursor_db_task.fetchone()
            if err_id is None:
                form_main.error_task.setText("Такого id задачи нету")
            else:
                window_upgrade_task.show()
                form_upgrade_task.error_new_task.setText("")
                cursor_db_task.execute("SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                                       "lead_time_one FROM tasks WHERE user_login = ? AND id= ?",
                                       [user_login, id_task])
                user_db_task.commit()

                rec = cursor_db_task.fetchall()
                for row in rec:
                    form_upgrade_task.name_task.setText(row[0])
                    form_upgrade_task.status_task.setCurrentText(row[1])
                    form_upgrade_task.description_task.setText(row[2])
                    form_upgrade_task.ball.setValue(int(row[3]))
                    form_upgrade_task.group_task.setText(row[4])
                    s = str(row[5])
                year_task = int(s[0])*1000+int(s[1])*100+int(s[2])*10+int(s[3])
                month_task = int(s[5])*10+int(s[6])
                day_task = int(s[8])*10+int(s[9])

                day = datetime.date(year_task, month_task, day_task)
                form_upgrade_task.lead_time.setDate(day)
                form_upgrade_task.id_task.setText(str(id_task))

        except sqlite3.Error as err:
            form_upgrade_task.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def delete_task():
    user_login = form_main.user_login.text()
    id_task = form_main.number_task.text()

    if not user_login or user_login == "Войдите в аккаунт" or not id_task:
        if not user_login or user_login == "Войдите в аккаунт":
            form_main.user_data.setText("Войдите в аккаунт")
        else:
            form_main.error_task.setText("Выберите задачу")
    else:
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            cursor_db_task.execute("SELECT id FROM tasks WHERE user_login = ? AND id = ?", [user_login, id_task])
            user_db_task.commit()
            err_id = cursor_db_task.fetchone()
            if err_id is None:
                form_main.error_task.setText("Такого id задачи нету")
            else:
                cursor_db_task.execute("SELECT id FROM tasks WHERE user_login = ?", [user_login])
                user_db_task.commit()
                none_name_task = cursor_db_task.fetchone()
                if none_name_task is None:
                    form_main.error_task.setText("Ошибка удаления")
                else:
                    cursor_db_task.execute("DELETE FROM tasks WHERE user_login = ? AND id = ?", [user_login, id_task])
                user_db_task.commit()

                form_main.error_task.setText("Успешно удалено")

                form_main.name_task.setText("")
                form_main.status_task.setText("")
                form_main.description_task.setText("")
                form_main.ball_2.setText("")
                form_main.group_task.setText("")
                form_main.date_task.setText("")
                form_main.number_task.setText("")
        except sqlite3.Error as err:
            form_new_task.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()
            restarter()


def accept_task():
    user_login = form_main.user_login.text()
    id_task = form_main.number_task.text()

    if not user_login or user_login == "Войдите в аккаунт" or not id_task:
        form_main.user_data.setText("Войдите в аккаунт")
    else:
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()
            cursor_db_task.execute("SELECT id FROM tasks WHERE user_login = ? AND id = ?", [user_login, id_task])
            user_db_task.commit()
            err_id = cursor_db_task.fetchone()
            if err_id is None:
                form_main.error_task.setText("Такого id задачи нету")
            else:
                cursor_db_task.execute("SELECT ball FROM users WHERE user_login = ?", [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()
                for row in rec:
                    ball_all = (int(row[0]))

                cursor_db_task.execute("SELECT ball_one FROM tasks WHERE user_login = ? AND id = ?", [user_login, id_task])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()
                for row in rec:
                    ball_plus = (int(row[0]))
                ball_all_plus = ball_all + ball_plus

                cursor_db_task.execute("UPDATE users SET ball = ? WHERE user_login = ?", [ball_all_plus, user_login])
                user_db_task.commit()

                cursor_db_task.execute("SELECT ball FROM users WHERE user_login = ?", [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()
                for row in rec:
                    ball = (int(row[0]))
                form_main.ball.setText(str(ball))

                cursor_db_task.execute("SELECT id FROM tasks WHERE user_login = ?", [user_login])
                user_db_task.commit()
                none_name_task = cursor_db_task.fetchone()
                if none_name_task is None:
                    form_main.error_task.setText("Ошибка удаления")
                else:
                    cursor_db_task.execute(
                        "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                        "lead_time_one FROM tasks WHERE user_login = ? AND id= ?",
                        [user_login, id_task])
                    user_db_task.commit()

                    rec = cursor_db_task.fetchall()
                    for row in rec:
                        name_task = row[0]
                        status_task = (row[1])
                        description_task = (row[2])
                        ball = (int(row[3]))
                        group_task = (row[4])
                        s = str(row[5])
                    year_task = int(s[0]) * 1000 + int(s[1]) * 100 + int(s[2]) * 10 + int(s[3])
                    month_task = int(s[5]) * 10 + int(s[6])
                    day_task = int(s[8]) * 10 + int(s[9])

                    day = datetime.date(year_task, month_task, day_task)
                    lead_time = day

                    task_db = [int(id_task), str(user_login), str(name_task), str(status_task),
                               str(description_task), int(ball), str(group_task), str(lead_time)]
                    cursor_db_task.execute(
                        "INSERT INTO tasks_old(id, user_login, name_task_one, status_task_one, description_task_one, "
                        "ball_one, group_task_one, lead_time_one) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", task_db)
                    user_db_task.commit()

                    cursor_db_task.execute("DELETE FROM tasks WHERE user_login = ? AND id = ?", [user_login, id_task])
                    user_db_task.commit()

                    form_main.error_task.setText("Успешно удалено")

                    form_main.name_task.setText("")
                    form_main.status_task.setText("")
                    form_main.description_task.setText("")
                    form_main.ball_2.setText("")
                    form_main.group_task.setText("")
                    form_main.date_task.setText("")
                    form_main.number_task.setText("")
                    restarter()

        except sqlite3.Error as err:
            form_new_task.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


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
                    form_main.user_login.setText(user_login)
                    user_login_1 = user_login
                    user_login = form_reg.user_login.setText("")
                    user_password = form_reg.user_password.setText("")

                    cursor_db_login.execute("UPDATE users SET auto_login = 0 WHERE auto_login = 1 ")
                    user_db_login.commit()

                    cursor_db_login.execute("UPDATE users SET auto_login = 1 WHERE user_login = ? ", [user_login_1])
                    user_db_login.commit()

                    restarter()
                    main_form()
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

                form_reg.user_login.setText(user_login)
                form_reg.user_password.setText(user_password)

                form_reg_one.user_login.setText("")
                form_reg_one.user_password.setText("")
                form_reg_one.first_name.setText("")
                form_reg_one.second_name.setText("")
                form_reg_one.patronymic.setText("")
                form_reg_one.position.setText("")
                form_reg_one.Error.setText("")
                window_reg_one.close()
                app_reg_one.closeAllWindows()
            else:
                form_reg_one.user_login.setText("")
                reg_one_close()

        except sqlite3.Error as err:
            form_reg_one.Error.setText(err)
        finally:
            cursor_db_reg.close()
            user_db_reg.close()


def item_click(item):

    str_task = item.text()
    str_num = int(len(str_task))
    number = 4

    while number < str_num and str_task[number] != " ":
        if number == 4:
            id_task = str_task[number]
        else:
            id_task = id_task + str_task[number]
        number = number + 1
    form_main.number_task.setText(id_task)
    user_login = form_main.user_login.text()
    id_task = form_main.number_task.text()
    try:
        user_db_task = sqlite3.connect("User_db.db")
        cursor_db_task = user_db_task.cursor()

        cursor_db_task.execute("SELECT id FROM tasks WHERE user_login = ? AND id = ?", [user_login, id_task])
        user_db_task.commit()
        err_id = cursor_db_task.fetchone()

        if err_id is None:
            form_main.error_task.setText("Такого id задачи нету")
        else:
            cursor_db_task.execute("SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                "lead_time_one FROM tasks WHERE user_login = ? AND id= ?", [user_login, id_task])
            user_db_task.commit()
            rec = cursor_db_task.fetchall()
            for row in rec:
                form_main.name_task.setText(row[0])
                form_main.status_task.setText(row[1])
                form_main.description_task.setText(row[2])
                form_main.ball_2.setText(str(row[3]))
                form_main.group_task.setText(row[4])
                s = str(row[5])

            year_task = int(s[0]) * 1000 + int(s[1]) * 100 + int(s[2]) * 10 + int(s[3])
            month_task = int(s[5]) * 10 + int(s[6])
            day_task = int(s[8]) * 10 + int(s[9])

            day = datetime.date(year_task, month_task, day_task)
            form_main.date_task.setText(str(day))
    except sqlite3.Error as err:
        form_new_task.error_new_task.setText(err)
    finally:
        cursor_db_task.close()
        user_db_task.close()


def date_click():
    form_main.tasks_list_day.clear()
    day_its = form_main.main_calendar.selectedDate()
    day_its_one = day_its.toPyDate()
    form_main.day_task.setText(str(day_its_one))

    user_login = form_main.user_login.text()
    if not user_login:
        form_main.user_data.setText("Войдите в аккаунт")
    else:
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            cursor_db_task.execute("SELECT id, name_task_one, status_task_one  FROM tasks WHERE"
                                   " user_login = ? AND lead_time_one = ?", [user_login, day_its_one])
            user_db_task.commit()

            rec = cursor_db_task.fetchall()
            for row in rec:
                new_str_task = "ID: " + (str(row[0])) + " Название задачи: " + (row[1]) + "\tСтатус: " + (row[2])
                form_main.tasks_list_day.addItem(str(new_str_task))

            # cursor_db_task.execute("SELECT id FROM tasks WHERE user_login = ? AND id = ?", [user_login, id_task])
            # user_db_task.commit()
            # err_id = cursor_db_task.fetchone()
            #
            # if err_id is None:
            #     form_main.error_task.setText("Такого id задачи нету")
            # else:
            #     cursor_db_task.execute(
            #         "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
            #         "lead_time_one FROM tasks WHERE user_login = ? AND id= ?", [user_login, id_task])
            #     user_db_task.commit()
            #     rec = cursor_db_task.fetchall()
            #     for row in rec:
            #         form_main.name_task.setText(row[0])
            #         form_main.status_task.setText(row[1])
            #         form_main.description_task.setText(row[2])
            #         form_main.ball_2.setText(str(row[3]))
            #         form_main.group_task.setText(row[4])
            #         s = str(row[5])
            #
            #     year_task = int(s[0]) * 1000 + int(s[1]) * 100 + int(s[2]) * 10 + int(s[3])
            #     month_task = int(s[5]) * 10 + int(s[6])
            #     day_task = int(s[8]) * 10 + int(s[9])
            #
            #     day = datetime.date(year_task, month_task, day_task)
            #     form_main.date_task.setText(str(day))
        except sqlite3.Error as err:
            form_main.error_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def filter_click():
    form_main.tasks_list.clear()
    sort = form_main.filter.currentText()
    user_login = form_main.user_login.text()

    if not user_login or user_login == "Войдите в аккаунт":
        form_main.user_data.setText("Войдите в аккаунт")
    else:
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()
            if sort == "ID по возрастанию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks WHERE user_login = ? ORDER BY id",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_main.tasks_list.addItem(str(new_str_task))
            elif sort == "Название по возрастанию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks WHERE user_login = ? ORDER BY name_task_one",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_main.tasks_list.addItem(str(new_str_task))
            elif sort == "Статус по возрастанию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks WHERE user_login = ? ORDER BY status_task_one",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_main.tasks_list.addItem(str(new_str_task))
            elif sort == "Группа по возрастанию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks WHERE user_login = ? ORDER BY group_task_one",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_main.tasks_list.addItem(str(new_str_task))
            elif sort == "Дата по возрастанию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks WHERE user_login = ? ORDER BY lead_time_one",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + " Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_main.tasks_list.addItem(str(new_str_task))
            elif sort == "ID по убыванию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks WHERE user_login = ? ORDER BY id DESC",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_main.tasks_list.addItem(str(new_str_task))
            elif sort == "Название по убыванию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks WHERE user_login = ? ORDER BY name_task_one DESC",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_main.tasks_list.addItem(str(new_str_task))
            elif sort == "Статус по убыванию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks WHERE user_login = ? ORDER BY status_task_one DESC",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_main.tasks_list.addItem(str(new_str_task))
            elif sort == "Группа по убыванию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks WHERE user_login = ? ORDER BY group_task_one DESC",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_main.tasks_list.addItem(str(new_str_task))
            elif sort == "Дата по убыванию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks WHERE user_login = ? ORDER BY lead_time_one DESC",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + " Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_main.tasks_list.addItem(str(new_str_task))

        except sqlite3.Error as err:
            form_main.error_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def task_old_open():
    form_task_old.tasks_list.clear()
    user_login = form_main.user_login.text()

    if not user_login or user_login == "Войдите в аккаунт":
        form_main.user_data.setText("Войдите в аккаунт")
    else:
        window_task_old.show()
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            cursor_db_task.execute(
                "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                "lead_time_one, id FROM tasks_old WHERE user_login = ?",
                [user_login])
            user_db_task.commit()
            rec = cursor_db_task.fetchall()

            for row in rec:
                ball_s = str(row[3])
                new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + (row[1]) \
                               + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                form_task_old.tasks_list.addItem(str(new_str_task))

        except sqlite3.Error as err:
            form_new_task.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def filter_click_task_old():
    form_task_old.tasks_list.clear()
    sort = form_task_old.filter.currentText()
    user_login = form_main.user_login.text()

    if not user_login or user_login == "Войдите в аккаунт":
        form_main.user_data.setText("Войдите в аккаунт")
    else:
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()
            if sort == "ID по возрастанию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks_old WHERE user_login = ? ORDER BY id",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()
                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_task_old.tasks_list.addItem(str(new_str_task))

            elif sort == "Название по возрастанию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks_old WHERE user_login = ? ORDER BY name_task_one",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_task_old.tasks_list.addItem(str(new_str_task))
            elif sort == "Статус по возрастанию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks_old WHERE user_login = ? ORDER BY status_task_one",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_task_old.tasks_list.addItem(str(new_str_task))
            elif sort == "Группа по возрастанию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks_old WHERE user_login = ? ORDER BY group_task_one",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_task_old.tasks_list.addItem(str(new_str_task))
            elif sort == "Дата по возрастанию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks_old WHERE user_login = ? ORDER BY lead_time_one",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + " Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_task_old.tasks_list.addItem(str(new_str_task))
            elif sort == "ID по убыванию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks_old WHERE user_login = ? ORDER BY id DESC",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_task_old.tasks_list.addItem(str(new_str_task))
            elif sort == "Название по убыванию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks_old WHERE user_login = ? ORDER BY name_task_one DESC",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_task_old.tasks_list.addItem(str(new_str_task))
            elif sort == "Статус по убыванию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks_old WHERE user_login = ? ORDER BY status_task_one DESC",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_task_old.tasks_list.addItem(str(new_str_task))
            elif sort == "Группа по убыванию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks_old WHERE user_login = ? ORDER BY group_task_one DESC",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_task_old.tasks_list.addItem(str(new_str_task))
            elif sort == "Дата по убыванию":
                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks_old WHERE user_login = ? ORDER BY lead_time_one DESC",
                    [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + " Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_task_old.tasks_list.addItem(str(new_str_task))

        except sqlite3.Error as err:
            form_main.error_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def task_old_close():
    window_task_old.close()


def task_old_open_admin():
    form_task_old.tasks_list.clear()
    user_login = form_admin.user_l.text()

    if not user_login:
        form_admin.error_new_task.setText("Выберите пользователя")
    else:
        window_task_old.show()
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            cursor_db_task.execute(
                "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                "lead_time_one, id FROM tasks_old WHERE user_login = ?",
                [user_login])
            user_db_task.commit()
            rec = cursor_db_task.fetchall()

            for row in rec:
                ball_s = str(row[3])
                new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + (row[1]) \
                               + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                form_task_old.tasks_list.addItem(str(new_str_task))

        except sqlite3.Error as err:
            form_new_task.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def admin_open():
    window_admin.show()
    form_admin.lead_time.setMinimumDate(datetime.date.today())

    try:
        form_admin.tasks_list_all.clear()
        form_admin.tasks_list_all_2.clear()
        user_db_task = sqlite3.connect("User_db.db")
        cursor_db_task = user_db_task.cursor()

        cursor_db_task.execute(
            "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
            "lead_time_one, id FROM tasks")
        user_db_task.commit()
        rec = cursor_db_task.fetchall()

        for row in rec:
            ball_s = str(row[3])
            new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + (row[1]) \
                           + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
            form_admin.tasks_list_all.addItem(str(new_str_task))
        # year_task = int(s[0]) * 1000 + int(s[1]) * 100 + int(s[2]) * 10 + int(s[3])
        # month_task = int(s[5]) * 10 + int(s[6])
        # day_task = int(s[8]) * 10 + int(s[9])

        cursor_db_task.execute(
            "SELECT first_name, second_name, position, ball, id FROM users")
        user_db_task.commit()
        rec = cursor_db_task.fetchall()

        for row in rec:
            ball_s = str(row[3])
            new_str_task = "ID: " + (str(row[4])) + " " + (str(row[0])) + " " + (row[1]) + "   " + (row[2]) + "   " + ball_s
            form_admin.tasks_list_all_2.addItem(str(new_str_task))

    except sqlite3.Error as err:
        form_new_task.error_new_task.setText(err)
    finally:
        cursor_db_task.close()
        user_db_task.close()


def create_new_task_admin():
    user_login = form_admin.user_l.text()
    name_task_one = form_admin.name_task.text()
    status_task_one = form_admin.status_task.currentText()
    description_task_one = form_admin.description_task.toPlainText()
    ball_one = form_admin.ball.text()
    group_task_one = form_admin.group_task.text()
    lead_time_one = form_admin.lead_time.date()
    lead_time_one_con = lead_time_one.toPyDate()

    if not user_login or not name_task_one or not status_task_one or not description_task_one or not ball_one \
            or not group_task_one or not lead_time_one:
        if not user_login:
            form_admin.error_new_task.setText("Выберите пользователя")
        else:
            form_admin.error_new_task.setText("Проверьте заполненость всех полей")
    else:
        try:
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            cursor_db_task.execute("SELECT user_login FROM tasks WHERE user_login = ? AND name_task_one = ?",
                                   [user_login, name_task_one])
            user_db_task.commit()
            none_name_task = cursor_db_task.fetchone()

            if none_name_task is None:
                task_db = [user_login, name_task_one, status_task_one, description_task_one, ball_one, group_task_one,
                           lead_time_one_con]
                cursor_db_task.execute(
                    "INSERT INTO tasks(user_login, name_task_one, status_task_one, description_task_one, "
                    "ball_one, group_task_one, lead_time_one ) VALUES(?, ?, ?, ?, ?, ?, ?)", task_db)
                user_db_task.commit()
                form_admin.error_new_task.setText("Задача создана")

                form_admin.tasks_list_all.clear()

                cursor_db_task.execute(
                    "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                    "lead_time_one, id FROM tasks WHERE user_login = ?", [user_login])
                user_db_task.commit()
                rec = cursor_db_task.fetchall()

                for row in rec:
                    ball_s = str(row[3])
                    new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + \
                                   (row[1]) + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
                    form_admin.tasks_list_all.addItem(str(new_str_task))

            else:
                form_admin.error_new_task.setText("Запись с таким названием уже имеется")
        except sqlite3.Error as err:
            form_admin.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def item_click_admin(item):

    form_admin.tasks_list_all.clear()
    str_task = item.text()
    str_num = int(len(str_task))
    number = 4

    while number < str_num and str_task[number] != " ":
        if number == 4:
            id_task = str_task[number]
        else:
            id_task = id_task + str_task[number]
        number = number + 1

    try:
        user_db_task = sqlite3.connect("User_db.db")
        cursor_db_task = user_db_task.cursor()

        cursor_db_task.execute(
            "SELECT user_login FROM users WHERE id = ?", [id_task])
        user_db_task.commit()

        user_login1 = cursor_db_task.fetchone()
        user_login = str(user_login1[0])

        form_admin.user_l.setText(str(user_login))

        cursor_db_task.execute(
            "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
            "lead_time_one, id FROM tasks WHERE user_login = ?", [user_login])
        user_db_task.commit()
        rec = cursor_db_task.fetchall()

        for row in rec:
            ball_s = str(row[3])
            new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + (row[1]) \
                           + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
            form_admin.tasks_list_all.addItem(str(new_str_task))
    except sqlite3.Error as err:
        form_admin.error_new_task.setText(err)
    finally:
        cursor_db_task.close()
        user_db_task.close()


def item_click_admin_one(item):

    user_login = form_admin.user_l.text()
    str_task = item.text()
    str_num = int(len(str_task))
    number = 4

    while number < str_num and str_task[number] != "Н":
        if number == 4:
            id_task = str_task[number]
        else:
            id_task = id_task + str_task[number]
        number = number + 1
    if not user_login or not id_task:
        form_admin.error_new_task.setText("Выберите пользователя")
    else:
        try:

            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            form_upgrade_task.error_new_task.setText("")
            cursor_db_task.execute("SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
                                   "lead_time_one FROM tasks WHERE user_login = ? AND id= ?",
                                   [user_login, id_task])
            user_db_task.commit()

            rec = cursor_db_task.fetchall()
            for row in rec:
                form_admin.name_task.setText(row[0])
                form_admin.status_task.setCurrentText(row[1])
                form_admin.description_task.setText(row[2])
                form_admin.ball.setValue(int(row[3]))
                form_admin.group_task.setText(row[4])
                s = str(row[5])
            year_task = int(s[0]) * 1000 + int(s[1]) * 100 + int(s[2]) * 10 + int(s[3])
            month_task = int(s[5]) * 10 + int(s[6])
            day_task = int(s[8]) * 10 + int(s[9])

            day = datetime.date(year_task, month_task, day_task)
            form_admin.lead_time.setDate(day)
            form_admin.id_task.setText(str(id_task))

        except sqlite3.Error as err:
            form_admin.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def upgrade_task_admin():
    id_task = form_admin.id_task.text()
    name_task_one = form_admin.name_task.text()
    status_task_one = form_admin.status_task.currentText()
    description_task_one = form_admin.description_task.toPlainText()
    ball_one = form_admin.ball.text()
    group_task_one = form_admin.group_task.text()
    lead_time_one = form_admin.lead_time.date()
    lead_time_one_con = lead_time_one.toPyDate()
    user_login = form_admin.user_l.text()

    if not name_task_one or not status_task_one or not description_task_one or not ball_one or not group_task_one or not lead_time_one:
        form_admin.error_new_task.setText("Проверьте заполненость всех полей")
    else:
        try:
            print("test1")
            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            cursor_db_task.execute("SELECT user_login FROM tasks WHERE user_login = ? AND id = ?",
                                   [user_login, id_task])
            user_db_task.commit()

            task_db = [name_task_one, status_task_one, description_task_one, ball_one, group_task_one,
                       lead_time_one_con, user_login, id_task]

            cursor_db_task.execute("UPDATE tasks SET name_task_one = ?, status_task_one = ?, description_task_one = ?,"
                                   " ball_one = ?, group_task_one = ?, lead_time_one = ? WHERE"
                                   " user_login = ? AND id = ?", task_db)
            user_db_task.commit()
            form_admin.error_new_task.setText("Успешно обновлено")

            restarter_admin()
        except sqlite3.Error as err:
            form_upgrade_task.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def delete_task_admin():
    user_login = form_admin.user_l.text()
    id_task = form_admin.id_task.text()

    if not user_login or user_login == "Войдите в аккаунт" or not id_task:
        if not user_login or user_login == "Войдите в аккаунт":
            form_admin.error_new_task.setText("Выберите пользователя")
        else:
            form_admin.error_new_task.setText("Выберите задачу")
    else:
        try:

            user_db_task = sqlite3.connect("User_db.db")
            cursor_db_task = user_db_task.cursor()

            cursor_db_task.execute("SELECT id FROM tasks WHERE user_login = ? AND id = ?", [user_login, id_task])
            user_db_task.commit()
            err_id = cursor_db_task.fetchone()
            if err_id is None:
                form_admin.error_new_task.setText("Такого id задачи нету")
            else:
                cursor_db_task.execute("SELECT id FROM tasks WHERE user_login = ?", [user_login])
                user_db_task.commit()
                none_name_task = cursor_db_task.fetchone()
                if none_name_task is None:
                    form_main.error_task.setText("Ошибка удаления")
                else:
                    cursor_db_task.execute("DELETE FROM tasks WHERE user_login = ? AND id = ?", [user_login, id_task])
                user_db_task.commit()

                form_admin.error_new_task.setText("Успешно удалено")

                form_admin.name_task.setText("")
                form_admin.description_task.setText("")
                form_admin.status_task.setCurrentText("Очень срочная")
                form_admin.ball.setValue(int(0))
                form_admin.group_task.setText("")
                now_date = datetime.date.today()
                form_admin.lead_time.setDate(now_date)
                form_admin.id_task.setText("")
                restarter_admin()
        except sqlite3.Error as err:
            form_new_task.error_new_task.setText(err)
        finally:
            cursor_db_task.close()
            user_db_task.close()


def restarter_admin():
    form_admin.tasks_list_all.clear()

    try:
        user_db_task = sqlite3.connect("User_db.db")
        cursor_db_task = user_db_task.cursor()
        user_login = form_admin.user_l.text()
        cursor_db_task.execute(
            "SELECT name_task_one, status_task_one, description_task_one, ball_one, group_task_one, "
            "lead_time_one, id FROM tasks WHERE user_login = ?", [user_login])
        user_db_task.commit()
        rec = cursor_db_task.fetchall()

        for row in rec:
            ball_s = str(row[3])
            new_str_task = "ID: " + (str(row[6])) + " " + "Название задачи: " + (row[0]) + "\tСтатус:" + (row[1]) \
                           + "\tГруппа: " + (row[4]) + "\tДата: " + (str(row[5]))
            form_admin.tasks_list_all.addItem(str(new_str_task))
    except sqlite3.Error as err:
        form_admin.error_new_task.setText(err)
    finally:
        cursor_db_task.close()
        user_db_task.close()


form_admin.delete_task.clicked.connect(delete_task_admin)
form_admin.upgrade_new_task.clicked.connect(upgrade_task_admin)
form_admin.tasks_list_all.itemClicked.connect(item_click_admin_one)
form_main.abmin_button.clicked.connect(admin_open)
form_admin.tasks_list_all_2.itemClicked.connect(item_click_admin)
form_admin.task_old.clicked.connect(task_old_open_admin)
form_admin.create_new_task.clicked.connect(create_new_task_admin)
form_task_old.filter_button.clicked.connect(filter_click_task_old)
form_task_old.task_old_close.clicked.connect(task_old_close)
form_main.task_old.clicked.connect(task_old_open)
form_main.filter_button.clicked.connect(filter_click)
form_main.tasks_list_day.itemClicked.connect(item_click)
form_main.main_calendar.selectionChanged.connect(date_click)
form_main.tasks_list.itemClicked.connect(item_click)
form_upgrade_task.upgrade_new_task.clicked.connect(upgrade_new_task)
form_main.upgrade_task_window_2.clicked.connect(upgrade_task)
form_main.delete_task_window.clicked.connect(delete_task)
form_main.accept_task_window.clicked.connect(accept_task)
form_main.restart.clicked.connect(restarter)
form_main.registration_window.clicked.connect(reg_open)
form_main.new_task_window.clicked.connect(new_task_open)
form_new_task.create_new_task.clicked.connect(create_new_task)
form_reg.register_button.clicked.connect(reg_one_open)
form_reg.login_button.clicked.connect(reg_close)
form_reg_one.login_button.clicked.connect(reg_one_close)

app_main.exec()

