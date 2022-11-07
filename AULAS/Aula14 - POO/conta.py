'''
class Conta: 
    #Atributos recebidos tipos
    titular = ''
    numero = 0
    saldo = 0
    limite = 0

    def __str__ (self): #Conta

        return f' {self.titular} - {self.numero} - {self.saldo} - {self.limite}'
'''

# Exercício 01
'''
class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

conta = Conta('Dieter', 21321321, 2500.00, 1000.00)

print(conta)
'''


# Exercício 02

class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

conta1 = Conta('Dieter', 21321321, 2500.00, 1000.00)
conta2 = Conta('Karla', 799879, 10500.00, 1000.00)
conta3 = Conta('Antonella', 9876521, 855500.00, 5000.00)

print(conta1)
print(conta2)
print(conta3)


