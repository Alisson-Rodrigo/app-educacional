# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


materias = [
    'Matemática',
    'Física',
    'História',
    'Geografia',
    'Filosofia',
    'Inglês',
    'Português',
    'Química',
    'Biologia',
    'Sociologia',
    'Artes',
    'Educação Física',
    'Redação'
]


class Ui_TelaPrincipal(object):
    def setupUi(self, TelaPrincipal):
        TelaPrincipal.setObjectName("TelaPrincipal")
        TelaPrincipal.setEnabled(True)
        TelaPrincipal.resize(900, 570)
        TelaPrincipal.setMinimumSize(QtCore.QSize(900, 550))
        TelaPrincipal.setMaximumSize(QtCore.QSize(900, 640))
        TelaPrincipal.setStyleSheet("background-color: rgb(30, 30, 30);")
        qtRectangle = TelaPrincipal.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        TelaPrincipal.move(qtRectangle.topLeft())
        self.centralwidget = QtWidgets.QWidget(TelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 220, 300, 330))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(300, 330))
        self.scrollArea.setStyleSheet("border: none;\n"
                                      "background-color: rgb(33, 33, 33);")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 281, 372))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtons = {}
        # self.materias(materias)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.background_foto = QtWidgets.QFrame(self.centralwidget)
        self.background_foto.setGeometry(QtCore.QRect(65, 20, 170, 170))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_foto.sizePolicy().hasHeightForWidth())
        self.background_foto.setSizePolicy(sizePolicy)
        self.background_foto.setMinimumSize(QtCore.QSize(170, 170))
        self.background_foto.setMaximumSize(QtCore.QSize(170, 170))
        self.background_foto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.background_foto.setStyleSheet("border-radius: 85px;\n"
"background-color: rgb(217, 217, 217);")
        self.background_foto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_foto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_foto.setObjectName("background_foto")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(300, 0, 600, 530))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setGeometry(QtCore.QRect(10, 10, 40, 20))
        self.botao_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sair.setStyleSheet("border-radius: 10px;\n"
"background-color: red;")
        self.botao_sair.setObjectName("botao_sair")
        TelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        TelaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaPrincipal)
        self.statusbar.setObjectName("statusbar")
        TelaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(TelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipal)
    
    def materias(self, materias):
        _translate = QtCore.QCoreApplication.translate
        for materia in materias:
            self.pushButtons[materia] = QtWidgets.QPushButton(
                self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setPointSize(24)
            self.pushButtons[materia].setFont(font)
            self.pushButtons[materia].setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButtons[materia].setStyleSheet("border-radius: 10px;\n"
                                                    "background-color: rgb(252, 88, 20);")
            self.pushButtons[materia].setObjectName(materia)
            self.verticalLayout.addWidget(self.pushButtons[materia])
            self.pushButtons[materia].setText(
                _translate("TelaPrincipal", materia))
        

    def retranslateUi(self, TelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipal.setWindowTitle(
            _translate("TelaPrincipal", "Tela Principal"))
        self.botao_sair.setText(_translate("TelaPrincipal", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_TelaPrincipal()
    ui.setupUi(TelaPrincipal)
    TelaPrincipal.show()
    sys.exit(app.exec_())
