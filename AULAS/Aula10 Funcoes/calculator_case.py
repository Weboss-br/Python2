from controller import *

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while True:

    operacao = input('Digite a operação: ')
    
    match operacao:
        case '+':
            print(f'Você digitou {num1} + {num2} e o resultado é: ')
            print(soma(num1,num2))
            break    

        case '-':
            print(f'Você digitou {num1} - {num2} e o resultado é: ')
            print(subtracao(num1,num2))
            break

        case '/':
            print(f'Você digitou {num1} / {num2} e o resultado é: ')        
            print(divisao(num1,num2))
            break    

        case '*':
            print(f'Você digitou {num1} * {num2} e o resultado é: ')  
            print(multiplicacao(num1,num2))
            break
