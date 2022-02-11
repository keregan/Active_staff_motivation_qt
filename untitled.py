from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(False)
        MainWindow.resize(801, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.completed_task = QtWidgets.QListView(self.centralwidget)
        self.completed_task.setGeometry(QtCore.QRect(30, 40, 221, 261))
        self.completed_task.setObjectName("completed_task")
        self.tasks_in_progress = QtWidgets.QListView(self.centralwidget)
        self.tasks_in_progress.setGeometry(QtCore.QRect(290, 40, 221, 261))
        self.tasks_in_progress.setObjectName("tasks_in_progress")
        self.new_tasks = QtWidgets.QListView(self.centralwidget)
        self.new_tasks.setGeometry(QtCore.QRect(550, 40, 221, 261))
        self.new_tasks.setObjectName("new_tasks")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(620, 20, 121, 16))
        self.label_3.setObjectName("label_3")
        self.user_data = QtWidgets.QLabel(self.centralwidget)
        self.user_data.setGeometry(QtCore.QRect(60, 410, 47, 13))
        self.user_data.setObjectName("user_data")
        self.post = QtWidgets.QLabel(self.centralwidget)
        self.post.setGeometry(QtCore.QRect(50, 430, 91, 16))
        self.post.setObjectName("post")
        self.registration_window = QtWidgets.QPushButton(self.centralwidget)
        self.registration_window.setGeometry(QtCore.QRect(40, 460, 75, 23))
        self.registration_window.setObjectName("registration_window")
        self.money = QtWidgets.QLabel(self.centralwidget)
        self.money.setGeometry(QtCore.QRect(160, 420, 61, 31))
        self.money.setObjectName("money")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 400, 111, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 400, 71, 16))
        self.label_8.setObjectName("label_8")
        self.weekend = QtWidgets.QLabel(self.centralwidget)
        self.weekend.setGeometry(QtCore.QRect(290, 430, 47, 13))
        self.weekend.setObjectName("weekend")
        self.progressBar_raise = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_raise.setGeometry(QtCore.QRect(450, 430, 321, 21))
        self.progressBar_raise.setProperty("value", 0)
        self.progressBar_raise.setObjectName("progressBar_raise")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(570, 400, 71, 21))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Выполненые задачи"))
        self.label_2.setText(_translate("MainWindow", "Задачи в процессе"))
        self.label_3.setText(_translate("MainWindow", "Новые задачи"))
        self.user_data.setText(_translate("MainWindow", "ФИО"))
        self.post.setText(_translate("MainWindow", "Должность"))
        self.registration_window.setText(_translate("MainWindow", "Вход"))
        self.money.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Выходные дни"))
        self.label_8.setText(_translate("MainWindow", "Заработок$$"))
        self.weekend.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Повышение"))

    def add_function(self):
        self.registration_window.click.connect(self.reg_window)

    def reg_window(self):
        r_window = QMessageBox()
        r_window.setWindowTitle("Вход в систему")
        r_window.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        r_window.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
