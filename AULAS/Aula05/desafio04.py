'''
Exercício-04 - Com base nas aulas passadas vamos criar um sorteio de lista e utilizando o conceito de estrutura de 
decisão exibir qual foi a posição de ordem de inserção de dados que foi sorteada! Usando o conceito de importação 
otimizada importe a função choice, logo em seguida crie quatro variáveis representadas por nomes n1, n2, n3, n4, 
essas variáveis devem ser do tipo string e devem solicitar dados. crie uma variável que receba como lista estas quatro 
variáveis. 

crie uma variável usando a importação otimizada e atribuindo a variável lista.

 crie uma função de impressão 
utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console. utilizando o conceito 
de interpolação exiba qual foi o nome sorteado. utilizando o conceito de estrutura de decisão cria uma condição que 
exiba a ordem em que foi digitado o nome sorteado pela variável de sorteio da lista!
'''

from random import choice

n1 = str(input('Digite algo: '))
n2 = str(input('Digite algo: '))
n3 = str(input('Digite algo: '))
n4 = str(input('Digite algo: '))
lista = [n1,n2,n3,n4]

#print('X'*5,'As palavras foram: \n', lista)

sorteado = choice(lista)

print('O nome do primeiro sorteado foi {}\n'.format(sorteado))

if sorteado == n1:
    print('O sorteado foi o primeiro')

if sorteado == n2:
    print('O sorteado foi o segundo')

if sorteado == n3:
    print('O sorteado foi o terceiro')

if sorteado == n4:
    print('O sorteado foi o quarto')