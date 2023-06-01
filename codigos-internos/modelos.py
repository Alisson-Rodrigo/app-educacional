import abc
import datetime


class Usuario(abc.ABC):
    def __init__(self, email, senha, nome, sobrenome, nascimento):
        self._email = email
        self._senha = senha
        self._nome = nome
        self._sobrenome = sobrenome
        self._nascimento = nascimento
        self._ultimo_login = None

    def get_email(self):
        return self._email

    @abc.abstractmethod
    def validar_email(self, email):
        pass

    @abc.abstractmethod
    def validar_senha(self, senha):
        pass


class Professor(Usuario):
    def __init__(self, email, senha, nome, sobrenome, nascimento):
        super().__init__(email, senha, nome, sobrenome, nascimento)

    def validar_email(self, email):
        if email.find("@") != -1:
            return True
        else:
            return False

    def validar_senha(self, senha):
        if self._senha == senha:
            return True
        else:
            return False


class Aluno(Usuario):
    def __init__(self, email, senha, nome, sobrenome, nascimento):
        super().__init__(email, senha, nome, sobrenome, nascimento)
        self._atividades_feitas = {}
        self._media = 0

    def validar_email(self, email):
        if email.find("@") != -1:
            return True
        else:
            return False

    def validar_senha(self, senha):
        if self._senha == senha:
            return True
        else:
            return False


class Materia:
    def __init__(self, nome, descricao, alunos, professor):
        self._nome = nome
        self._descricao = descricao
        self._professor = professor
        self._alunos = alunos
        self._lista_atividades = []


class Atividade:
    def __init__(self, materia, autor, titulo, descricao, questoes):
        self._materia = materia
        self._autor = autor
        self._titulo = titulo
        self._descricao = descricao
        self._questoes = questoes
        self._data = datetime.datetime.now()


class Questao:
    def __init__(self, atividade, enunciado, resposta):
        self._atividade = atividade
        self._enunciado = enunciado
        self._resposta = resposta

    def valida_resposta(self, resposta):
        if resposta == self._resposta:
            return True
        else:
            return False


if __name__ == "__main__":
    u = Professor("jorge@example.com", "jorge1234", "jorge", "luis", "2003-09-01")
