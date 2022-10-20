'''Crie uma variável com valor fixo. Esta variável deve conter um numero que não interfira na decisão de um índice
Crie uma variavel recebendo o conceito de polimorfismo com o sinal de igual.
Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabeçalho 
    adicione quebra de linha, ao final.

Crie um laço de repetição, este laço deve solicitar ao usuário para digitar um número por 3 vezes..

Dentro do laço, crie a capacidade de soma entre esses números digitados, eles devem ser atributos de soma.
Crie uma função de impressão usando máscara de substituição e imprima de forma descritiva a soma desses números.
Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize 
    como rodapé, definindo o fim do laço de repetição.
Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabeçalho 
    início estrutura de decisão adicione quebra de linha, ao final.
Crie uma estrutura de decisão falando se a soma desses números é maior que 10, menor que 10, igual a dez, diferente de 10.
Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize 
    como rodapé, definindo o fim da estrutura de decisão.
'''
from time import sleep

soma = 0
a = '='*5

print(f'{a} CABEÇALHO {a}\n')

for c in range (0,3,1):
    b=int(input('Escreva algo: '))
    soma=soma+b

print('A soma entre os valores digitados foi: {}'.format(soma))

print(f'{a} MEIO {a}\n')

if soma >10:
    print('Maior que 10 e diferente de 10')
elif soma==10:
    print('Igual 10')
elif soma<10:
    print('Menor que 10 e diferente de 10')
elif soma!=10:
    print('O número é diferente de 10')

print(f'{a} Rodape {a}\n')