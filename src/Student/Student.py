class Student:

    def __init__(self, nome, matricula, nota, faltas):

        self.nome = nome
        self.matricula = matricula
        self.nota = nota
        self.faltas = faltas

    def somaNota(self, notas):

        self.nota += notas / 4

        return self.nota

    def somaFaltas(self, Faltas):

        self.faltas += Faltas

        return self.faltas

    def __str__(self):

        return f"Dados do estudante: \n Nome: {self.nome} \n Matricula: {self.matricula} \n Nota: {self.nota} \n Faltas: {self.faltas}"