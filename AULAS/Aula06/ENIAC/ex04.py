'''
Crie uma variável com valor fixo esta variável deve conter um numero que não interfira na decisão de um índice
Crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.
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
CONSTANTE = 8

poli = "="*20


lista = []

soma = 0

for c in range(0, 3):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    soma += numero

print(" {} + {} + {} = {} ".format(lista[0],lista[1],lista[2],soma))

print(f"\n{poli} RODAPE {poli}\n")

print(f"\n{poli} CABECALHO ESTRUTURA DECISAO {poli}\n")

if soma > 10:
    print("A soma é maior que 10")
elif soma < 10:
    print("A soma é inferior a 10")
else:
    print("A soma é igual a 10")

if soma != 10:
    print("A soma é diferente de 10")

print(f"\n{poli} RODAPE ESTRUTURA DECISAO {poli}")