'''3-EXERCÍCIO: Crie variáveis com tipos predefinidos, utilizando a função de inserção de dados, fica a seu critério a 
utilização de nomes de variáveis, crie no mínimo 4 variáveis, usando máscara de substituição atribua estas variáveis as 
suas respectivas descrições'''

num1 = int(input('Digite um número: '))
decimal = float(input('Digite um float .: '))
txt = str(input('Digite um texto: '))
trueorfalse = bool(input('Digite, True or False: '))

#Esse exemplo é mascara
print('X'*15,'RESULTADO','X'*15)
print('Você digitou corretamente: \nForam digitados: {}, {}, {}, e {}'.format(num1,decimal,txt,trueorfalse))