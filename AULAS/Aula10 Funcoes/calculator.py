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
