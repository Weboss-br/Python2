#Estudo de listas

import random

n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))

lista = [n1, n2, n3, n4]

#A (lista) está sendo utilizada como OBJETO
sorteado = random.choice(lista)

print('O nome do primeiro sorteado foi {}\n'.format(sorteado))
sorteado = random.choice(lista)
print('O nome do segundo sorteado foi {}\n'.format(sorteado))
sorteado = random.choice(lista)
print('O nome do terceiro sorteado foi {}\n'.format(sorteado))
sorteado = random.choice(lista)
print('O nome do quarto sorteado foi {}\n'.format(sorteado))