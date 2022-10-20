'''
Exercício-02 - Usando a biblioteca interna random use o conceito de importação de toda biblioteca. Crie 
quatro variáveis recebendo valores, essas variáveis devem ser com tipos predefinidos tipo string, crie 
uma variável recebendo uma lista das 4 variáveis, logo em seguida utilize importação da biblioteca e 
atribua a função embaralhar(shuffle). Essa importação irá realizar o embaralhamento dos valores 
recebidos atribua a lista a esta função. Crie uma função de impressão utilizando polimorfismo e quebra 
de linhas para definir um cabeçalho para sua aplicação console. utilizando a interpolação exiba em 
seguida com a função de impressão a ordem definida dos nomes da variável lista.
'''
from random import shuffle

var1 = str(input('Digite um texto: '))
var2 = str(input('Digite um texto: '))
var3 = str(input('Digite um texto: '))
var4 = str(input('Digite um texto: '))

lista = [var1,var2,var3,var4]

shuffle(lista)

print('X'*5,'O Resultado do embaralhamento é: {}'.format(lista))

print(f'O Resultado do embaralhamento é: {lista}')


