class Aluno:
    def __init__(self, nome=""):
        self.nome = nome

class Turma:
    def __init__(self, nome="", ano=0, alunos=[]):
        self.nome = nome
        self.ano = ano
        self.alunos = alunos