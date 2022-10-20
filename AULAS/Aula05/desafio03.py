'''
Exercício-03 - Com base nas aulas passadas vamos criar uma calculadora utilizando o conceito de estrutura de decisão. 
Crie duas variáveis recebendo dados numéricos com casas decimais, a descrição deve ser relacionada com primeira nota e 
segunda nota! Crie uma variável para realizar este cálculo, não esqueça de utilizar o conceito de ordem de procedência 
aritmética. Crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua 
aplicação console. Utilizando máscara de substituição imprima de forma descritiva a primeira nota, utilize quebra de 
linha, imprima a segunda nota, utilize a quebra de linha e imprima o resultado. Usando estrutura de decisão crie uma 
condição onde o resultado for maior que sete imprima na sua aplicação console que este aluno está acima da média.
Usando estrutura de decisão crie uma condição onde o resultado for igual a sete imprima na sua aplicação console que 
este aluno está na média. 

Usando estrutura de decisão crie uma condição onde o resultado for entre cinco e sete imprima 
na sua aplicação console que este aluno pode solicitar recuperação. 

Usando estrutura de decisão crie uma condição onde o 
resultado for entre quatro e cinco imprima na sua aplicação console que este aluno deve procurar o professor. Usando 
estrutura de decisão crie uma condição de saída e imprima na sua aplicação console que este aluno infelizmente não 
atingiu o esperado!
'''
##################
 
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1+nota2)/2

print('X'*5, 'RESUNTADOS \n\n A primeira nota é: {},\n a segunda nota é {}.\n Portanto sua média é: {} \n'.format(nota1,nota2,media))

if media >= 7.1:
    print('O aluno está acima da média')
if media == 7:
    print('Está com 7')
if media <= 6.9 and media >= 5:
    print('O aluno pegou recuperação')
if media <= 4.9 and media >= 0:
    print('O aluno rodou')

################################
'''
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1+nota2)/2

print('X'*5, 'RESUNTADOS \n\n A primeira nota é: {},\n a segunda nota é {}.\n Portanto sua média é: {} \n'.format(nota1,nota2,media))

if media >= 7.1:
    print('O aluno está acima da média')
elif media == 7:
    print('Sua nota está na média')
elif media >=5 <7:
    print('O aluno pegou recuperação')
elif media >=4 ==5:
    print('Vai falar com o professor')
else:
    print('O aluno rodou')
'''