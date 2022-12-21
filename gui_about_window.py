from PyQt5 import QtCore, QtGui, QtWidgets


class UiAbout(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(300, 210)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        About.setMinimumSize(QtCore.QSize(300, 210))
        About.setMaximumSize(QtCore.QSize(300, 210))
        self.text_aboutProgramm = QtWidgets.QLabel(About)
        self.text_aboutProgramm.setGeometry(QtCore.QRect(0, 0, 300, 210))
        self.text_aboutProgramm.setMinimumSize(QtCore.QSize(300, 210))
        self.text_aboutProgramm.setMaximumSize(QtCore.QSize(300, 210))
        self.text_aboutProgramm.setStyleSheet("color: rgb(255, 255, 255);\n""font: 75 8pt \"MS Shell Dlg 2\";")
        self.text_aboutProgramm.setWordWrap(True)
        self.text_aboutProgramm.setObjectName("text_aboutProgramm")
        self.fon_label = QtWidgets.QLabel(About)
        self.fon_label.setGeometry(QtCore.QRect(0, 0, 300, 230))
        self.fon_label.setMinimumSize(QtCore.QSize(300, 230))
        self.fon_label.setMaximumSize(QtCore.QSize(300, 230))
        self.fon_label.setText("")
        self.fon_label.setPixmap(QtGui.QPixmap("Background/FonLow.jpg"))
        self.fon_label.setScaledContents(True)
        self.fon_label.setObjectName("fon_label")
        self.fon_label.raise_()
        self.text_aboutProgramm.raise_()
        self.retranslateUi(About)

        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle("О программе DProject")
        About.setWindowIcon(QtGui.QIcon("Background/DP.jpg"))
        self.text_aboutProgramm.setText(_translate("About", "<html><head/><body>"
                                                            "<p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">DProject</span></p>"
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Release: 14/05/2022</span></p>"
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">(build 1.0.4)</span></p>"
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Author: Ozerov Yaroslav, DP</span></p>"
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">email: ozerovyaroslav25@gmail.com</span></p>"
                                                            "<p align=\"center\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:11pt;\">© </span><span style=\" font-size:11pt;\">2022 SPb</span></p>"
                                                            "</body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = UiAbout()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())
