from fila import Fila

supermercado = Fila()
banco = Fila()
loterica = Fila()

banco.entrar('Clay')
banco.entrar('jow')

print(banco.fila)
