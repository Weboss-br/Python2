#Estudo de listas

#Importando apenas um a função da biblioteca random
import random from shuffle

n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print('Segue o embaralhamento: {}\n'.format(lista))
