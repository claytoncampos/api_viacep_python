class Empregados:

    def __init__(self, nome, salario, funcao):
        self.nome = nome
        self.salario = salario
        self.funcao = funcao
        self.email = nome + '@email.com'

    def calc_salario_anual(self):
        return self.salario * 12


emp1 = Empregados('Antonio', 3000, 'Analista')
emp2 = Empregados('Pedro', 5000, 'Engenheiro')


print(emp1.calc_salario_anual())
print(emp2.funcao)

print(str(Empregados.calc_salario_anual(emp2)) + ' ' + emp2.funcao)
