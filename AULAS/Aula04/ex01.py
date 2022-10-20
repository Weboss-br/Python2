'''validador = True
# Substituição do valor inicial
validador = False

idade = int(input('Digite sua idade: '))

print(' '*15, 'Expressão de igualdade', ' '*15,'\n')
# Criação de variável booleana através de expressão de igualdade

validador = ( idade == 18)
print(validador)


print(' '*15, 'Expressão de diferença', ' '*15,'\n')

# Criação de variável booleana através de expressão da diferença
validador = ( idade != 18 )
print(validador)


print(' '*15, 'Expressão de maior ', ' '*15,'\n')
#Criação de variável booleana atraves de expressão de maior
validador = ( idade > 18 )
print(validador)

print(' '*15, 'Expressão de menor ', ' '*15,'\n')

#Criação de variável booleana através de expressão da menor
validador = ( idade < 18 )
print(validador)

print(' '*15, 'Expressão de maior e igual', ' '*15,'\n')
#Criação de variável booleana através de expressão da maior e igual
validador = ( idade >= 18 )
print(validador)

print(' '*15, 'Expressão de menor e igual ', ' '*15,'\n')
# Criação de variáveis booleana atraves de expressão de menor e igual
validador = ( idade <= 18 )
print(validador)'''

#Minha forma de resolver

validador = bool()

idade = int(input('Digite sua idade: '))

print('Expressão de igualdade')
validador = ( idade == 18)
print(validador)

print('Expressão de diferença')
validador = ( idade != 18 )
print(validador)

print('Expressão de maior ')
validador = ( idade > 18 )
print(validador)

print('Expressão de menor ')
validador = ( idade < 18 )
print(validador)

print('Expressão de maior e igual')
validador = ( idade >= 18 )
print(validador)

print('Expressão de menor e igual ')
validador = ( idade <= 18 )
print(validador)