## The program is used to work with a database of tasks with users in an interface form, with elements of motivation, progress and the ability to control.

To clone the repository, you need to enter the command in the console:

    $ git clone https://github.com/keregan/Active_staff_motivation_qt.git

Further use requires:

    import hashlib
    import datetime
    import time
    import sqlite3
    import tkinter
    from tkinter import *
    from PIL import Image
    from PyQt5 import uic
    from PyQt5.QtWidgets import QApplication, QTableWidgetItem
    from PyQt5.uic.properties import QtCore

Additionally, the program requires:

1. To work with sqlite3 databases
2. Script to reformat **ui** to **py** to work with individual objects of the interface program
3. QT Designer, to create an interface, but is optional

Instructions for using the program are contained in the file: [doc_ru.docx](https://github.com/keregan/Active_staff_motivation_qt/blob/master/doc_ru.docx)

Examples of interface use of the program:

1. Login to the program

    ![Header](https://github.com/keregan/Active_staff_motivation_qt/blob/master/Image/account_login.png)

2. Registration user

    ![Header](https://github.com/keregan/Active_staff_motivation_qt/blob/master/Image/registration.png)

3.  Main page of the program

    ![Header](https://github.com/keregan/Active_staff_motivation_qt/blob/master/Image/main_window.png)

4.  Adding a task (deleting, adding and executing are similar in functionality and interface)

    ![Header](https://github.com/keregan/Active_staff_motivation_qt/blob/master/Image/add_task.png)

5.  Administration mode (the ability to control and manage the tasks of other users)

    ![Header](https://github.com/keregan/Active_staff_motivation_qt/blob/master/Image/administrator_mode.png)



