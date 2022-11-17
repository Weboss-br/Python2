from model import Conta
from controller import create, read

a1 = Conta()
a1.titular = 'Marcio Kratos'
a1.numero = '123456789'
a1.saldo = 3000.0

create(a1)

lista_a1 = read()

print(lista_a1)

print("*"*30)

for c in lista_a1:
    print(c)