from PyQt5 import QtCore, QtGui, QtWidgets

# host,login,pass,domen,link
lst_p = [['login1', 'pass1', 'host1', 'domen1', 'link1'], ['login2', 'pass2', 'host2', 'domen2', 'link2'],
         ['login3', 'pass3', 'host3', 'domen3', 'link3']]


class UiMainWindow(object):

    # Задание всех окон и панелей
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.save_prof_1 = QtWidgets.QAction(MainWindow)
        self.save_prof_2 = QtWidgets.QAction(MainWindow)
        self.save_prof_3 = QtWidgets.QAction(MainWindow)
        self.about_help = QtWidgets.QAction(MainWindow)
        self.about_action = QtWidgets.QAction(MainWindow)
        self.action_exit_butt = QtWidgets.QAction(MainWindow)
        self.mainYab = QtWidgets.QWidget()
        self.lastTab = QtWidgets.QWidget()
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menu = QtWidgets.QMenu(self.menubar)
        self.Help = QtWidgets.QMenu(self.menubar)
        self.reference = QtWidgets.QMenu(self.menubar)
        self.button_execute_n2 = QtWidgets.QPushButton(self.lastTab)
        self.checkBox_check_update = QtWidgets.QCheckBox(self.lastTab)
        self.checkBox_remove = QtWidgets.QCheckBox(self.lastTab)
        self.checkBox_conclusion_dir = QtWidgets.QCheckBox(self.lastTab)
        self.label = QtWidgets.QLabel(self.lastTab)
        self.button_check_connection = QtWidgets.QPushButton(self.mainYab)
        self.button_open_side = QtWidgets.QPushButton(self.mainYab)
        self.button_prof_3 = QtWidgets.QPushButton(self.mainYab)
        self.button_prof_2 = QtWidgets.QPushButton(self.mainYab)
        self.button_prof_1 = QtWidgets.QPushButton(self.mainYab)
        self.button_Help = QtWidgets.QPushButton(self.mainYab)
        self.button_Execute = QtWidgets.QPushButton(self.mainYab)
        self.menu_file = QtWidgets.QMenu(self.menu)
        self.line_Link = QtWidgets.QLineEdit(self.mainYab)
        self.text_link = QtWidgets.QLabel(self.mainYab)
        self.text_Domen = QtWidgets.QLabel(self.mainYab)
        self.text_Host_IP = QtWidgets.QLabel(self.mainYab)
        self.text_Pass = QtWidgets.QLabel(self.mainYab)
        self.line_Domen = QtWidgets.QLineEdit(self.mainYab)
        self.line_Host = QtWidgets.QLineEdit(self.mainYab)
        self.line_Pass = QtWidgets.QLineEdit(self.mainYab)
        self.line_Login = QtWidgets.QLineEdit(self.mainYab)
        self.FON = QtWidgets.QLabel(self.mainYab)
        self.window_communication = QtWidgets.QTextBrowser(self.mainYab)
        self.button_clear = QtWidgets.QPushButton(self.mainYab)
        self.text_Login = QtWidgets.QLabel(self.mainYab)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        MainWindow.setEnabled(True)
        MainWindow.resize(600, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 420))
        MainWindow.setMaximumSize(QtCore.QSize(600, 420))
        MainWindow.setStyleSheet("")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 602, 402))
        self.tabWidget.setMinimumSize(QtCore.QSize(602, 402))
        self.tabWidget.setMaximumSize(QtCore.QSize(602, 402))
        self.tabWidget.setStyleSheet("border-color: rgb(204, 162, 150);")
        self.tabWidget.setObjectName("tabWidget")
        self.mainYab.setStyleSheet(
            "/*background-image: url(\"Background/FonLow.jpg\");\n""background-size: cover;*/\n""")
        self.mainYab.setObjectName("mainYab")
        self.text_Login.setGeometry(QtCore.QRect(30, 30, 51, 21))

        self.text_Login.setFont(font)
        self.text_Login.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_Login.setObjectName("text_Login")
        self.button_clear.setGeometry(QtCore.QRect(25, 230, 101, 31))

        self.button_clear.setFont(font)
        self.button_clear.setStyleSheet("background-color: rgb(102, 152, 153);\n""color: rgb(255, 255, 255);")
        self.button_clear.setObjectName("Clear_window")
        self.window_communication.setGeometry(QtCore.QRect(25, 270, 546, 90))
        self.window_communication.setObjectName("window_communication")
        self.FON.setGeometry(QtCore.QRect(0, 0, 602, 402))
        self.FON.setMinimumSize(QtCore.QSize(602, 402))
        self.FON.setMaximumSize(QtCore.QSize(602, 402))
        self.FON.setStyleSheet("background-image: url(Background/FonLow.jpg);")
        self.FON.setText("")
        self.FON.setPixmap(QtGui.QPixmap("Background/FonLow.jpg"))
        self.FON.setObjectName("FON")
        self.line_Login.setGeometry(QtCore.QRect(110, 30, 150, 22))

        self.line_Login.setFont(font)
        self.line_Login.setObjectName("line_Login")
        self.line_Pass.setGeometry(QtCore.QRect(110, 60, 150, 22))

        self.line_Pass.setFont(font)
        self.line_Pass.setObjectName("line_Pass")
        self.line_Host.setGeometry(QtCore.QRect(110, 90, 150, 22))

        self.line_Host.setFont(font)
        self.line_Host.setObjectName("line_Host")
        self.line_Domen.setGeometry(QtCore.QRect(110, 120, 150, 22))

        self.line_Domen.setFont(font)
        self.line_Domen.setObjectName("line_Domen")
        self.text_Pass.setGeometry(QtCore.QRect(30, 60, 51, 21))

        self.text_Pass.setFont(font)
        self.text_Pass.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_Pass.setObjectName("text_Pass")
        self.text_Host_IP.setGeometry(QtCore.QRect(30, 90, 51, 21))

        self.text_Host_IP.setFont(font)
        self.text_Host_IP.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_Host_IP.setObjectName("text_Host_IP")
        self.text_Domen.setGeometry(QtCore.QRect(30, 120, 51, 21))

        self.text_Domen.setFont(font)
        self.text_Domen.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_Domen.setObjectName("text_Domen")
        self.text_link.setGeometry(QtCore.QRect(30, 150, 51, 21))

        self.text_link.setFont(font)
        self.text_link.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_link.setObjectName("text_link")
        self.line_Link.setGeometry(QtCore.QRect(110, 150, 150, 22))

        self.line_Link.setFont(font)
        self.line_Link.setObjectName("line_Link")
        self.button_Execute.setGeometry(QtCore.QRect(450, 230, 121, 31))

        self.button_Execute.setFont(font)
        self.button_Execute.setStyleSheet("background-color: rgb(102, 152, 153);\n""color: rgb(255, 255, 255);")
        self.button_Execute.setObjectName("button_Execute")
        self.button_Help.setGeometry(QtCore.QRect(470, 150, 101, 31))

        self.button_Help.setFont(font)
        self.button_Help.setStyleSheet("background-color: rgb(102, 152, 153);\n""color: rgb(255, 255, 255);")
        self.button_Help.setObjectName("button_Help")
        self.button_prof_1.setGeometry(QtCore.QRect(288, 30, 101, 31))

        self.button_prof_1.setFont(font)
        self.button_prof_1.setStyleSheet("background-color: rgb(102, 152, 153);\n""color: rgb(255, 255, 255);")
        self.button_prof_1.setObjectName("button_prof_1")
        self.button_prof_2.setGeometry(QtCore.QRect(288, 70, 101, 31))

        self.button_prof_2.setFont(font)
        self.button_prof_2.setStyleSheet("background-color: rgb(102, 152, 153);\n""color: rgb(255, 255, 255);")
        self.button_prof_2.setObjectName("button_prof_2")

        self.button_prof_3.setGeometry(QtCore.QRect(288, 110, 101, 31))

        self.button_prof_3.setFont(font)
        self.button_prof_3.setStyleSheet("background-color: rgb(102, 152, 153);\n""color: rgb(255, 255, 255);")
        self.button_prof_3.setObjectName("button_prof_3")

        self.button_open_side.setGeometry(QtCore.QRect(414, 30, 156, 31))
        self.button_open_side.setFont(font)
        self.button_open_side.setStyleSheet("background-color: rgb(102, 152, 153);\n""color: rgb(255, 255, 255);")
        self.button_open_side.setObjectName("button_open_side")

        self.button_check_connection.setGeometry(QtCore.QRect(414, 70, 156, 31))
        self.button_check_connection.setFont(font)
        self.button_check_connection.setStyleSheet(
            "background-color: rgb(102, 152, 153);\n""color: rgb(255, 255, 255);")
        self.button_check_connection.setObjectName("button_check_connection")

        self.tabWidget.addTab(self.mainYab, "")

        self.lastTab.setStyleSheet("\n""")
        self.lastTab.setObjectName("lastTab")

        self.label.setGeometry(QtCore.QRect(0, 0, 601, 381))
        self.label.setStyleSheet("background-image: url(Background/FonLow.jpg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Background/FonLow.jpg"))
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")

        self.checkBox_conclusion_dir.setGeometry(QtCore.QRect(20, 50, 400, 21))
        self.checkBox_conclusion_dir.setObjectName("checkBox")
        self.checkBox_conclusion_dir.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_remove.setGeometry(QtCore.QRect(20, 70, 400, 21))
        self.checkBox_remove.setObjectName("checkBox")
        self.checkBox_remove.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_check_update.setGeometry(QtCore.QRect(20, 90, 400, 21))
        self.checkBox_check_update.setObjectName("checkBox")
        self.checkBox_check_update.setStyleSheet("color: rgb(255, 255, 255);")

        self.button_execute_n2.setGeometry(QtCore.QRect(480, 320, 101, 31))
        self.button_execute_n2.setFont(font)
        self.button_execute_n2.setStyleSheet("background-color: rgb(102, 152, 153);\n""color: rgb(255, 255, 255);")
        self.button_execute_n2.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.lastTab, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.reference.setObjectName("reference")
        self.Help.setObjectName("Help")
        MainWindow.setMenuBar(self.menubar)

        self.about_action.setObjectName("action_2")
        self.reference.addAction(self.about_action)
        self.menu.setObjectName("menu")
        self.menu_file.setObjectName("menu_file")

        self.save_prof_1.setObjectName("save_prof_1")
        self.save_prof_2.setObjectName("save_prof_2")
        self.save_prof_3.setObjectName("save_prof_3")

        self.action_exit_butt.setObjectName("action_3")
        self.menu_file.addAction(self.save_prof_1)
        self.menu_file.addAction(self.save_prof_2)
        self.menu_file.addAction(self.save_prof_3)
        self.menu.addAction(self.menu_file.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit_butt)
        self.menubar.addAction(self.menu.menuAction())

        self.about_help.setObjectName("action_help")
        self.reference.addAction(self.about_help)
        self.reference.addSeparator()

        self.menubar.addAction(self.reference.menuAction())
        self.menubar.addAction(self.Help.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.FON.raise_()
        self.text_Login.raise_()
        self.button_clear.raise_()
        self.button_execute_n2.raise_()
        self.window_communication.raise_()
        self.line_Login.raise_()
        self.line_Pass.raise_()
        self.line_Host.raise_()
        self.line_Domen.raise_()
        self.text_Pass.raise_()
        self.text_Host_IP.raise_()
        self.text_Domen.raise_()
        self.text_link.raise_()
        self.line_Link.raise_()
        self.button_Execute.raise_()
        self.button_Help.raise_()
        self.button_prof_1.raise_()
        self.button_prof_2.raise_()
        self.button_prof_3.raise_()
        self.button_open_side.raise_()
        self.button_check_connection.raise_()
        self.checkBox_conclusion_dir.raise_()
        self.checkBox_remove.raise_()
        self.checkBox_check_update.raise_()

    # Задание всех окон и панелей
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("DP - универсальный помощник")
        MainWindow.setWindowIcon(QtGui.QIcon("Background/DP.jpg"))
        self.text_Login.setText(_translate("MainWindow", "Логин:"))
        self.button_clear.setText(_translate("MainWindow", "Очистить"))
        self.window_communication.setHtml(_translate("MainWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\"> Добро пожаловать в универсальный помощник DP!</span></p>\n"
                                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p></body></html>"))
        self.text_Pass.setText(_translate("MainWindow", "Пароль:"))
        self.text_Host_IP.setText(_translate("MainWindow", "Host/IP:"))
        self.text_Domen.setText(_translate("MainWindow", "Домен:"))
        self.text_link.setText(_translate("MainWindow", "link:"))
        self.button_Execute.setText(_translate("MainWindow", "Загрузить сайт"))
        self.button_Help.setText(_translate("MainWindow", "Помощь"))
        self.button_prof_1.setText(_translate("MainWindow", "Профиль 1"))
        self.button_prof_2.setText(_translate("MainWindow", "Профиль 2"))
        self.button_prof_3.setText(_translate("MainWindow", "Профиль 3"))
        self.button_open_side.setText(_translate("MainWindow", "Открыть сайт"))
        self.button_check_connection.setText(_translate("MainWindow", "Проверка соединения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainYab), _translate("MainWindow", "Данные"))
        self.checkBox_conclusion_dir.setText(_translate("MainWindow", "Вывести содержимое корневой директории сервера"))
        self.checkBox_remove.setText(_translate("MainWindow", "Удалить файлы загруженного сайта"))
        self.checkBox_check_update.setText(_translate("MainWindow", "Произвести обновление системы"))
        self.button_execute_n2.setText(_translate("MainWindow", "Выполнить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lastTab), _translate("MainWindow", "доп. функции"))
        self.reference.setTitle(_translate("MainWindow", "Справка"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_file.setTitle(_translate("MainWindow", "Записать данные в"))
        self.action_exit_butt.setText(_translate("MainWindow", "Выход"))
        self.about_action.setText(_translate("MainWindow", "О программе"))
        self.about_help.setText(_translate("MainWindow", "Помощь"))
        self.save_prof_1.setText(_translate("MainWindow", "Профиль 1"))
        self.save_prof_2.setText(_translate("MainWindow", "Профиль 2"))
        self.save_prof_3.setText(_translate("MainWindow", "Профиль 3"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
