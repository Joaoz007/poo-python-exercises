class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

class Matricula:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

print ("--Aluno--")
aluno1 = Aluno("João Silva", "2023001", "Engenharia")
aluno2 = Aluno("Maria Oliveira", "2023002", "Medicina")

print ("--Matricula--")
matricula1 = Matricula("Cálculo I", "MAT101", 60)
matricula2 = Matricula("Anatomia", "MED201", 80)