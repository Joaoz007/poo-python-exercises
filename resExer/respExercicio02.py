class Aluno:
    def __init__(self, nome, matricula, curso, notas=None):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = [] if notas is None else notas

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def status(self):
        media = self.calcular_media()
        if media >= 7.0:
            print("Aprovado")
        else:
            print("Reprovado")

