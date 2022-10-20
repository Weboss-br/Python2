'''
Exercício-01 - Usando a biblioteca interna random use o conceito de importação otimizada de (Escolha (Choice)) de lista, 
crie quatro variáveis recebendo valores, essas variáveis devem ser com tipos predefinidos tipo string, crie uma variável 
recebendo uma lista das 4 variáveis, logo em seguida crie outra variável recebendo a importação, essa importação irá 
realizar o sorteio de um valor recebido. Crie uma função de impressão utilizando polimorfismo e quebra de linhas para 
definir um cabeçalho para sua aplicação console. Utilizando a interpolação exiba em seguida com a função de impressão o 
nome sorteado pela biblioteca random.
'''
from random import choice


n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
n3 = int(input('Mais um: '))
n4 = int(input('Esse é o último: '))

lista = [n1, n2, n3, n4]

sorteado = random.choice(lista)
print(' '*15, 'O nome do primeiro sorteado foi {}\n'.format(sorteado))

#sorteado = random.choice(lista)
#print(' '*15, 'O nome do segundo sorteado foi {}\n'.format(sorteado))
#sorteado = random.choice(lista)
#print(' '*15, 'O nome do terceiro sorteado foi {}\n'.format(sorteado))
#sorteado = random.choice(lista)
#print(' '*15, 'O nome do quarto sorteado foi {}\n'.format(sorteado))