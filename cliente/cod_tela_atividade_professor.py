# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_AtividadeProfessor_professor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from teste_questao import AtividadeQuestao
from modelos import Atividade, Questao


class Ui_AtividadeProfessor(object):
    def setupUi(self, AtividadeProfessor, atividade=None):
        self.atividade = atividade
        AtividadeProfessor.setObjectName("AtividadeProfessor")
        AtividadeProfessor.resize(900, 580)
        AtividadeProfessor.setMinimumSize(QtCore.QSize(900, 580))
        AtividadeProfessor.setMaximumSize(QtCore.QSize(900, 580))
        AtividadeProfessor.setStyleSheet("background-color: rgb(51, 51, 51);")
        qtRectangle = AtividadeProfessor.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        AtividadeProfessor.move(qtRectangle.topLeft())
        self.scrollArea = QtWidgets.QScrollArea(AtividadeProfessor)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 861, 491))
        self.scrollArea.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, -38, 843, 577))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_titulo = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.input_titulo.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.input_titulo.setFont(font)
        self.input_titulo.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_titulo.setText("")
        self.input_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.input_titulo.setObjectName("input_titulo")
        self.verticalLayout.addWidget(self.input_titulo)
        self.input_descricao = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.input_descricao.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_descricao.setFont(font)
        self.input_descricao.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_descricao.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.input_descricao.setObjectName("input_descricao")
        self.verticalLayout.addWidget(self.input_descricao)
        self.questoes = {}
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.botao_voltar = QtWidgets.QPushButton(AtividadeProfessor)
        self.botao_voltar.setGeometry(QtCore.QRect(0, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_voltar.setFont(font)
        self.botao_voltar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_voltar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_voltar.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.botao_voltar.setObjectName("botao_voltar")
        self.layoutWidget = QtWidgets.QWidget(AtividadeProfessor)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 530, 861, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.botao_add_questao = QtWidgets.QPushButton(self.layoutWidget)
        self.botao_add_questao.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_add_questao.setFont(font)
        self.botao_add_questao.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_add_questao.setStyleSheet("border: 3px solid rgb(7, 66, 22);\n"
                                             "background-color: rgb(255, 255, 255);")
        self.botao_add_questao.setObjectName("botao_add_questao")
        self.horizontalLayout_2.addWidget(self.botao_add_questao)
        self.botao_publicar = QtWidgets.QPushButton(self.layoutWidget)
        self.botao_publicar.setMinimumSize(QtCore.QSize(0, 30))
        self.botao_publicar.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.botao_publicar.setFont(font)
        self.botao_publicar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_publicar.setStyleSheet("border: none;\n"
                                          "border-radius: 15px;\n"
                                          "background-color: rgb(0, 166, 202);")
        self.botao_publicar.setObjectName("botao_publicar")
        self.horizontalLayout_2.addWidget(self.botao_publicar)
        for q in atividade.questoes if atividade and atividade.questoes else []:
            num = len(self.questoes)
            self.questoes[num] = AtividadeQuestao(
                self.scrollAreaWidgetContents, num + 1, q.enunciado, [q.letra_a, q.letra_b, q.letra_c, q.letra_d, q.letra_e], q.id)
            self.verticalLayout.addWidget(self.questoes[num])

        self._translate = QtCore.QCoreApplication.translate
        self.botao_add_questao.clicked.connect(
            self.botao_add_nova_questao_funcao)
        self.retranslateUi(AtividadeProfessor)
        QtCore.QMetaObject.connectSlotsByName(AtividadeProfessor)

    def botao_add_nova_questao_funcao(self):
        num = len(self.questoes)
        self.questoes[num] = AtividadeQuestao(
            self.scrollAreaWidgetContents, num + 1)
        self.questoes[num].input_enunciado.setPlaceholderText(
            self._translate("AtividadeProfessor", "Enunciado"))
        self.questoes[num].input_letra['A'].setPlaceholderText(
            self._translate("AtividadeProfessor", "A"))
        self.questoes[num].input_letra['B'].setPlaceholderText(
            self._translate("AtividadeProfessor", "B"))
        self.questoes[num].input_letra['C'].setPlaceholderText(
            self._translate("AtividadeProfessor", "C"))
        self.questoes[num].input_letra['D'].setPlaceholderText(
            self._translate("AtividadeProfessor", "D"))
        self.questoes[num].input_letra['E'].setPlaceholderText(
            self._translate("AtividadeProfessor", "E"))
        self.verticalLayout.addWidget(self.questoes[num])

    def retranslateUi(self, AtividadeProfessor):
        AtividadeProfessor.setWindowTitle(self._translate(
            "AtividadeProfessor", "Cadastrar Atividade"))
        self.input_titulo.setPlaceholderText(
            self._translate("AtividadeProfessor", "Título"))
        self.input_descricao.setPlaceholderText(
            self._translate("AtividadeProfessor", "Descrição"))
        self.botao_add_questao.setText(
            self._translate("AtividadeProfessor", "+"))
        self.botao_publicar.setText(
            self._translate("AtividadeProfessor", "Publicar"))
        self.botao_voltar.setText(self._translate("Atividade", "←"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AtividadeProfessor = QtWidgets.QWidget()
    ui = Ui_AtividadeProfessor()
    ui.setupUi(AtividadeProfessor, Atividade(1, 'função afim', 'atividade de função', 1, 1, 1, [
        Questao(2, 1, 'Em 1988, o Brasil promulgou a Constituição que rege o país até hoje. Sobre a Constituição de 1988, é correto afirmar que:',
                'a', 'a', 'b', 'c', 'd', 'e'),
        Questao(3, 1, 'Após a promulgação da Constituição de 1988, o Brasil passou a ser regido por uma nova Carta Magna. Sobre a Constituição de 1988, é correto afirmar que:', 'a', 'a', 'b', 'c', 'd', 'e'),
    ]))
    AtividadeProfessor.show()
    sys.exit(app.exec_())
