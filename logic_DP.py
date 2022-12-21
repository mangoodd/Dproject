import json
import smtplib
import webbrowser

import paramiko
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog

import gui_DP_window
from gui_about_window import UiAbout
from gui_help_window import UiHelp

lst_p = [['login1', 'pass1', 'host1', 'domen1', 'link1'], ['login2', 'pass2', 'host2', 'domen2', 'link2'],
         ['login3', 'pass3', 'host3', 'domen3', 'link3']]
window_condition = ''

command = 'telnet localhost 22'
command_to_start1 = 'sudo apt install ufw && sudo apt-get install python-certbot-nginx ' \
                    '-y && sudo apt install zip unzip && sudo apt-add-repository -y ppa:hda-me/nginx-stable ' \
                    '&& sudo apt-get install brotli nginx nginx-module-brotli && sudo systemctl unmask nginx.service ' \
                    '&& mkdir -p /var/www/side/html && cd /var/www/side/html'
command_to_start2 = 'unzip site && rm site'


class ExamplesAbout(QtWidgets.QMainWindow, gui_DP_window.UiMainWindow):

    def __init__(self):

        super().__init__()

        # Сценарии
        self.setupUi(self)
        self.action_exit_butt.triggered.connect(self.exit_e)
        self.button_prof_1.clicked.connect(lambda: self.open_save_prof(1))
        self.button_prof_2.clicked.connect(lambda: self.open_save_prof(2))
        self.button_prof_3.clicked.connect(lambda: self.open_save_prof(3))
        self.button_open_side.clicked.connect(self.open_side)
        self.button_check_connection.clicked.connect(self.check_connection_command)
        self.button_clear.clicked.connect(self.clear_window)
        self.button_Execute.clicked.connect(self.ls_command)
        self.about_action.triggered.connect(self.open_about)
        self.button_Help.clicked.connect(self.open_help)
        self.about_help.triggered.connect(self.open_help)
        self.save_prof_1.triggered.connect(lambda: self.save_prof(1))
        self.save_prof_2.triggered.connect(lambda: self.save_prof(2))
        self.save_prof_3.triggered.connect(lambda: self.save_prof(3))

    # Открытие сайта
    def open_side(self):
        lst = self.copy_data()
        w = lst[0]
        link = 'http://' + w
        webbrowser.open(link, new=2)

    # Очистка диалогового окна
    def clear_window(self):
        global window_condition
        window_condition = ''
        self.window_communication.setText(window_condition)

    # Вывод новой записи в диалоговое окно
    def window_record(self, new_record):
        global window_condition
        window_condition += '\n' + new_record
        self.window_communication.setText(window_condition)

    # Выход из программы
    @staticmethod
    def exit_e():
        sys.exit(app.exec_())

    # Выполнение команд на сервере
    def command_to_server(self, host, login, secret, order, printable_flag):
        _translate = QtCore.QCoreApplication.translate
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=host, username=login, port=22, password=secret)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(order)
            data = str(ssh_stdout.read().decode('UTF-8'))
            self.clear_window()
            if printable_flag:
                self.window_record(f'Выполнение команды: {order} \n')
                self.window_record(data)
            ssh.close()
            return True
        except paramiko.ssh_exception.AuthenticationException:
            self.clear_window()
            self.window_record("Неверные данные аутентификации: логин или пароль введены не верно!")
            return False
        except paramiko.ssh_exception.BadAuthenticationType:
            self.clear_window()
            self.window_record("Необходимо использовать открытый ключ!")
            return False
        except smtplib.socket.gaierror:
            self.clear_window()
            self.window_record("Нет ответа от сервера. Неверно введено имя хоста/ip или введенный сервер не отвечает. ")
            return False
        except paramiko.SSHException:
            self.clear_window()
            self.window_record("SSH недоступен. Проверьте включен ли SSH? ")
            return False
        finally:
            pass

    # Получение данных из локальных переменных
    def chech_data(self):
        lst = list(self.copy_data())
        if lst[0] == '' or lst[0] == '' or lst[0] == '':
            return False
        else:
            return True

    # Копирование данных из полей "Логин","Пароль","hostIP"
    def copy_data(self):
        if self.line_Login.text():
            login = self.line_Login.text()
            pas = self.line_Pass.text()
            ip = self.line_Host.text()
            domen = self.line_Domen.text()
            link = self.line_Link.text()
            lst = [ip.replace(' ', ''), login.replace(' ', ''), pas.replace(' ', ''), domen.replace(' ', ''),
                   link.replace(' ', '')]
            return lst
        else:
            lst = []
            for i in range(5):
                lst.append('')
            return lst

    # Проверка соединения по введеным данным в окно ввода
    def check_connection_command(self):
        printable_flag = False
        host, login, secret, domen, link = self.copy_data()
        flag_check_data = self.chech_data()
        if flag_check_data:
            flag = self.command_to_server(host, login, secret, 'cd / ls-l', printable_flag)
            if flag:
                self.window_record('Соединение установлено!')
        else:
            self.window_record('Данные пользователя не введены или введены не верно! Проверьте окно ввода ')

    # Выполнение команды ls на сервере и вывод результата
    def ls_command(self):
        global command_to_start1, command_to_start2
        printable_flag = True
        host, login, secret, domen, link = self.copy_data()
        flag_check_data = self.chech_data()
        command_to_run = command_to_start1 + ' && ' + 'wget -O site https://getfile.dokpub.com/yandex/get/' + link + ' && ' + command_to_start2
        if flag_check_data and len(link) > 10 and 'https://' in link:
            self.window_record('Загрузка началась и может занимать несколько минут.')
            flag = self.command_to_server(host, login, secret, command_to_run, printable_flag)
            if flag:
                self.window_record(
                    '-------------------------------------------------------------'
                    '-----------------------------------------------')
                self.window_record('Operation complete! Сайт загружен на сервер.\n Для проверки нажмите "Открыть сайт"')
        elif len(link) < 10 or 'https://' not in link:
            self.window_record('Ссылка на скачивание файла не указана или указана не верно. Проверьте поле "link" ')
        else:
            self.window_record('Данные пользователя не введены или введены не верно! Проверьте окно ввода ')

    # Вызов окна "о программе"
    @staticmethod
    def open_about():
        widget = QDialog()
        about = UiAbout()
        about.setupUi(widget)
        widget.exec_()

    # Вызов окна "Помощь"
    @staticmethod
    def open_help():
        widget = QDialog()
        help_w = UiHelp()
        help_w.setupUi(widget)
        widget.exec_()

    # Сохранение введенный данных в профиль (host,login,pass,bomen,link)
    def save_prof(self, number_prof):
        global lst_p
        lst = self.copy_data()
        if lst[0] != '' and lst[1] != '' and lst[2] != '':
            with open('profiles.json', 'r') as f:
                profiles_read = json.load(f)
            profiles_read[lst_p[number_prof - 1][1]] = lst[1]
            profiles_read[lst_p[number_prof - 1][2]] = lst[2]
            profiles_read[lst_p[number_prof - 1][0]] = lst[0]
            profiles_read[lst_p[number_prof - 1][3]] = lst[3]
            profiles_read[lst_p[number_prof - 1][4]] = lst[4]
            with open('profiles.json', 'w') as f:
                json.dump(profiles_read, f)
            stroka = str(f'Данные пользователя {profiles_read[lst_p[number_prof - 1][1]]} успешно записаны в профиль')
            self.window_record(stroka)
        else:
            self.window_record("Введите данные для сохранения (Логин, Пароль, Host/IP)")

    # Открытие данных профиля и запись в окно ввода
    def open_save_prof(self, number_prof):
        with open('profiles.json', 'r') as f:
            profiles_read = json.load(f)
        self.line_Login.setText(profiles_read[lst_p[number_prof - 1][1]])
        self.line_Pass.setText(profiles_read[lst_p[number_prof - 1][2]])
        self.line_Host.setText(profiles_read[lst_p[number_prof - 1][0]])
        self.line_Domen.setText(profiles_read[lst_p[number_prof - 1][3]])
        self.line_Link.setText(profiles_read[lst_p[number_prof - 1][4]])
        if profiles_read[lst_p[number_prof - 1][1]] == '' or profiles_read[lst_p[number_prof - 1][1]] == '' or \
                profiles_read[lst_p[number_prof - 1][2]] == '' or profiles_read[lst_p[number_prof - 1][0]] == '':
            self.window_record(f"Этот профиль пуст")
        else:
            self.window_record(f"Вы загрузили данные профиля {profiles_read[lst_p[number_prof - 1][1]]}")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = ExamplesAbout()
    form.show()
    app.exec_()
