import mysql.connector as mysql


tabelas = {}
tabelas['usuarios'] = (
    "CREATE TABLE IF NOT EXISTS sistema_educacional.usuarios ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "email VARCHAR(255) NOT NULL,"
    "senha VARCHAR(255) NOT NULL,"
    "nome VARCHAR(255) NOT NULL,"
    "sobrenome VARCHAR(255) NOT NULL,"
    "nascimento DATE NOT NULL,"
    "UNIQUE (email)"
    ")"
)
tabelas['professores'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.professores ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'usuario_id INT NOT NULL,'
    'FOREIGN KEY (usuario_id) REFERENCES usuarios(id)'
    ')'
)
tabelas['alunos'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.alunos ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'usuario_id INT NOT NULL,'
    'FOREIGN KEY (usuario_id) REFERENCES usuarios(id)'
    ')'
)
tabelas['materias'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.materias ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'nome VARCHAR(255) NOT NULL,'
    'descricao VARCHAR(255) NOT NULL,'
    'professor_id INT NOT NULL,'
    'FOREIGN KEY (professor_id) REFERENCES professores(id)'
    ')'
)
tabelas['atividades'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.atividades ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'nome VARCHAR(255) NOT NULL,'
    'descricao VARCHAR(255) NOT NULL,'
    'materia_id INT NOT NULL,'
    'FOREIGN KEY (materia_id) REFERENCES materias(id)'
    ')'
)
tabelas['questoes'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.questoes ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'enunciado VARCHAR(255) NOT NULL,'
    'resposta VARCHAR(255) NOT NULL,'
    'atividade_id INT NOT NULL,'
    'FOREIGN KEY (atividade_id) REFERENCES atividades(id)'
    ')'
)


class SistemaEducacional:
    def __init__(self):
        self._usuario = None
        self._mydb = mysql.connect(
            host="localhost",
            user="root",
            password="1234",
            auth_plugin='mysql_native_password'
        )
        self._cursor = self._mydb.cursor()
        self._sql = "CREATE DATABASE IF NOT EXISTS sistema_educacional"
        self._cursor.execute(self._sql, multi=True)

        for tabela in tabelas:
            self._cursor.execute(tabelas[tabela])

        self._mydb.commit()

    def cadastrar(self, email, senha, nome, sobrenome, nascimento):
        pass

    def login(self, email, senha):
        pass

    def logout(self):
        self._usuario = None


if __name__ == "__main__":
    sistema = SistemaEducacional()
