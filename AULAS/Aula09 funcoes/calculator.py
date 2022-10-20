# Utilizando os conhecimentos adquiridos nas aulas anteriores onde foram feitos códigos estruturados, estamos 
# incrementando o Python funcional. crie um projeto com o nome Calculadora python, depois crie um documento chamado 
# controller dentro deste documento deve conter 4 funções com as operações básicas matemáticas. crie um outro documento 
# chamado main, este documento deve estar importando as 4 operações matemáticas. crie uma função print solicitando dados 
# ao usuário esta funcao deve ser com tipo predefinido tipo flutuante. deve ser utilizado o conceito de interpolação para 
# criar um cabeçalho de um menu, dentro deste menu deve conter a possibilidade de fazer a impressão dos dados inseridos 
# pelo usuário, permitindo assim o usuário escolher uma das 4 operações matemáticas importadas, consequentemente 
# imprimindo assim o resultado desejado dos dados inseridos. 

from controller import *

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while True:

    operacao = input('Digite a operação: ')
    if operacao == 'soma' or operacao == '+':
        print(f'Você digitou {num1} + {num2} e o resultado é: ')
        print(soma(num1,num2))
        break    

    if operacao == 'subtracao' or operacao == '-':
        print(f'Você digitou {num1} - {num2} e o resultado é: ')
        print(subtracao(num1,num2))
        break

    if operacao == 'divisao' or operacao == '/':
        print(f'Você digitou {num1} / {num2} e o resultado é: ')        
        print(divisao(num1,num2))
        break    

    if operacao == 'multiplicacao' or operacao == '*':
        print(f'Você digitou {num1} * {num2} e o resultado é: ')  
        print(multiplicacao(num1,num2))
        break
