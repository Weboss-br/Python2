from model import Conta
from controller import create, read

a1 = Conta()
a1.titular = 'Dieter Heiss'
a1.numero = '1616161'
a1.saldo = 15000.0

create(a1)

lista_a1 = read()

print(lista_a1)

print("*"*30)

for c in lista_a1:
    print(c)