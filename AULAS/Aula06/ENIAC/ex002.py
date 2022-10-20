'''
Crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.

Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string 
cabeçalho adicione quebra de linha, ao final.

Imprima no terminal o índice de repetição.

Crie um laço de repetição para imprimir a função print com a palavra FELIZ DIA DO PROGRAMADOR. a frase deve ser 
impressa 10 vezes.

Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois do string 
utilize como rodapé.
'''
poli = ('=')*10

#Interpolação
print(f'\n{poli} CABEÇALHO {poli}\n')

for i in range (0, 10, 2):
    print('FELIZ DIA DO PROGRAMADOR')

print(f'\n{poli} RODAPÉ {poli}\n')