from PyQt5 import QtCore, QtGui, QtWidgets


class UiHelp(object):
    def setupUi(self, Dialog):
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        Dialog.setObjectName("Dialog")
        Dialog.resize(588, 620)
        Dialog.setMinimumSize(QtCore.QSize(588, 620))
        Dialog.setMaximumSize(QtCore.QSize(588, 620))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 588, 640))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Background/FonLow.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(2, 2, 606, 620))
        self.textBrowser.setAccessibleDescription("")
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("border-image: url(Background/FonLow.jpg);\n"
                                       "selection-color: rgb(0, 0, 0);\n"
                                       "selection-background-color: rgb(255, 255, 255);\n"
                                       "alternate-background-color: rgb(85, 255, 0);\n"
                                       "color: rgb(255, 255, 255);")
        self.textBrowser.setTabChangesFocus(False)
        self.textBrowser.setOpenExternalLinks(False)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle("Помощь")
        Dialog.setWindowIcon(QtGui.QIcon("Background/DP.jpg"))
        self.label_2.setText(_translate("Dialog", "Помощь"))
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DProject - помощь"))
        self.textBrowser.setHtml(_translate("Dialog",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Помощь</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">------------------------------------------------------------------------------------------------------------------</span><span style=\" font-size:10pt; font-weight:600;\">ВАЖНО! ДАННАЯ ВЕРСИЯ ПРОГРАММЫ ПОДДЕРЖИВАЕТ СЕРВЕРА ПОД УПРАВЛЕНИЕМ ОС UBUNTU ВЕРСИИ 18.04</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">-----------------------------------------------------------------------------------------------</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Для успешной загрузки сайта на сервер заполните поля: &quot;Логин&quot;, &quot;Пароль&quot;, &quot;Host/IP&quot;, &quot;link&quot; и нажмите клавишу &quot;Загрузить сайт&quot;. Появление надписи &quot;Operation complete! Сайт загружен на сервер.&quot; в диалоговом окне, сообщит о успешном завершении загрузки. </span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Для проверки работоспособности сайта нажмите клавишу &quot;Открыть сайт&quot;.</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">________________________________________________________________________</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Окно ввода данных</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Background/window_insert.png\" /></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">&quot;Логин&quot; -</span><span style=\" font-size:10pt;\"> поле для ввода логина (имени пользователя), предоставляемое хостингом или измененное в процессе настройки сервера.</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">&quot;Пароль&quot; - </span><span style=\" font-size:10pt;\">поле для ввода пароля, предоставляемое хостингом.</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">&quot;Host/IP&quot; - </span><span style=\" font-size:10pt;\">поле для ввода ip адреса сервера, предоставляемое хостингом.</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">&quot;Domen&quot; </span><span style=\" font-size:10pt;\">(необязательное поле) - поле для ввода доменного имени устанавливаемого сайта.</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">&quot;link&quot; - </span><span style=\" font-size:10pt;\">поле для ввода ссылка на скачивание корневой папки с сайтом.</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">________________________________________________________________________</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Назначение клавиш:</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">&quot;Профиль 1&quot;,&quot;Профиль 2&quot;,&quot;Профиль 3&quot;</span><span style=\" font-size:10pt;\"> - кнопки для загрузки сохраненных данных профилей.</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">&quot;Загрузить сайт&quot;</span><span style=\" font-size:10pt;\"> - настройка сервера и загрузка сайта на сервер.</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">&quot;Открыть сайт&quot;</span><span style=\" font-size:10pt;\"> - открытие сайта в браузере по умолчанию.</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">&quot;Проверка соединения&quot;</span><span style=\" font-size:10pt;\"> - проверка связи с сервером.</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">&quot;Очистить&quot;</span><span style=\" font-size:10pt;\"> - очистка диалогового окна.</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">&quot;Помощь&quot;</span><span style=\" font-size:10pt;\"> - вывод документации по использованию программы.<br /></span><span style=\" font-size:10pt; font-weight:600;\">________________________________________________________________________</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Как сохранить/перезаписать данные профиля?</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Введите данные в окна &quot;Логин&quot;, &quot;Пароль&quot;, &quot;Host/IP&quot;. В пункте меню &quot;Файл&quot; --&gt; &quot;Сохранить в&quot; --&gt; выберите профиль для сохранения</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Background/window_save.png\" /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Как загрузить данные из профиля?</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Нажмите на клавишу профиля. В окне ввода появтся данные записанные в профиль.</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UiHelp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
