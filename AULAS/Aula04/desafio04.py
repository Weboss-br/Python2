''''04-EXERCÍCIO: Crie variáveis com tipos predefinidos que suportem a inserção de dados com casas decimais representando
os 4 últimos salários de uma (pessoa). crie uma variável para realizar a soma entre estes salários. crie uma função de 
impressão de dados para definir o cabeçalho de uma calculadora, utilizando o conceito de polimorfismo imprima a palavra 
Calculadora no centro da sua aplicação console, Logo em seguida use apenas uma vez a função de impressão, descreva cada 
campo com uma máscara de substituição, Ex " primeira variável : {} " os dados devem ser apresentados um em cada linha na 
sua aplicação console, deve ser utilizado os caracteres especiais de quebra de linha e na impressão deve apresentar 
apenas duas casas após a vírgula imprima no final utilizando a variável de soma para imprimir o resultado final do seu 
exercício.'''
sal1 = float(input('Salário 01: '))
sal2 = float(input('Salário 02: '))
sal3 = float(input('Salário 03: '))
sal4 = float(input('Salário 04: '))
sum = sal1+sal2+sal3+sal4

print('X'*15,'Calc','X'*15)

print('O salário do primeiro mês foi {:.2f},\n Do segundo foi {:.2f},\n Do terceiro foi {:.2f},\n Do quarto foi {:.2f},\n Somando tudo deu {:.2f}.'.format(sal1, sal2, sal3, sal4, sum))

