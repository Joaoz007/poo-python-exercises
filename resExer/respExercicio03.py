class Professor:
    def __init__(self, salario, nome, departamento):
        self.nome = nome
        self._salario = salario
        self.departamento = departamento

    def get_salario(self):
        return self._salario
    
    def set_salario(self, valor):
        if valor >= 0:
            self._salario = valor
        else:
            print("Salário não pode ser negativo")

print ("--Professor--")
professor1 = Professor(5000, "Carlos Pereira", "Matemática")