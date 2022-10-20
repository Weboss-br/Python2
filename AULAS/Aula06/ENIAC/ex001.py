'''
Crie uma variável do tipo inteiro recebendo dados;

Crie uma variável fazendo o cálculo do resto da divisão, usando máscara de substituição e realize a atribuição do 
valor;

Crie uma estrutura de condição onde irá imprimir no terminal se o cálculo da divisão é ímpar ou par.
'''

num1 = int(input('Escreva um numero: '))
#Fiz dessa forma(12 e 13), mas para o cód. ficar mais limpo, corrigi para a linha 14
#num2 = 2
#res = num1 % num2

res = num1 % 2

#Máscara de substituição:
print('Na divisão o resto é {}'.format(res))

if res == 0:
    print('O número {} é PAR.'.format(num1))

else:
    print('O número {} é IMPAR.'.format(num1))