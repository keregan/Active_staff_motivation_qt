# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kareg\PycharmProjects\Active_staff_motivation_qt\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Win_reg(object):
    def setupUi(self, Win_reg):
        Win_reg.setObjectName("Win_reg")
        Win_reg.resize(208, 113)
        Win_reg.setMinimumSize(QtCore.QSize(208, 113))
        Win_reg.setMaximumSize(QtCore.QSize(208, 113))
        self.layoutWidget = QtWidgets.QWidget(Win_reg)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 178, 48))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.user_login = QtWidgets.QLineEdit(self.layoutWidget)
        self.user_login.setObjectName("user_login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.user_login)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.user_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.user_password.setObjectName("user_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.user_password)
        self.response_to_user = QtWidgets.QLabel(Win_reg)
        self.response_to_user.setGeometry(QtCore.QRect(70, 60, 81, 20))
        self.response_to_user.setObjectName("response_to_user")
        self.splitter = QtWidgets.QSplitter(Win_reg)
        self.splitter.setGeometry(QtCore.QRect(30, 80, 150, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.login_button = QtWidgets.QPushButton(self.splitter)
        self.login_button.setObjectName("login_button")
        self.register_button = QtWidgets.QPushButton(self.splitter)
        self.register_button.setObjectName("register_button")

        self.retranslateUi(Win_reg)
        QtCore.QMetaObject.connectSlotsByName(Win_reg)

    def retranslateUi(self, Win_reg):
        _translate = QtCore.QCoreApplication.translate
        Win_reg.setWindowTitle(_translate("Win_reg", "Вход"))
        self.label.setText(_translate("Win_reg", "Логин"))
        self.label_2.setText(_translate("Win_reg", "Пароль"))
        self.response_to_user.setText(_translate("Win_reg", "Вход в систему"))
        self.login_button.setText(_translate("Win_reg", "Войти"))
        self.register_button.setText(_translate("Win_reg", "Регистрация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Win_reg = QtWidgets.QWidget()
    ui = Ui_Win_reg()
    ui.setupUi(Win_reg)
    Win_reg.show()
    sys.exit(app.exec_())
