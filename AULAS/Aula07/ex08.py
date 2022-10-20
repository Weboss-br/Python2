from time import sleep

media = 0
while media > 7:
    nome = str(input('Digite seu nome: '))
    sobreNome = str(input('Digite seu sobrenome: '))
    idade = int(input('Digite sua idade: '))
    media = 0
 
    for lista in range(0,2):
        nota = int(input('Digite sua nota'))
        lista_notas = [nota]
    
situacao = 'Reprovado'

if media >= 7:
    sleep(2)
    print('*')
    situacao = 'Aprovado'

dicionario_alunos = {'Nome':nome, 'Sobrenome':sobreNome, 'Idade':idade, 'Situacao':situacao}
print(f"{dicionario_alunos['Nome']} {dicionario_alunos['Sobrenome']} {dicionario_alunos['Idade']} - {dicionario_alunos['Situacao']} {dicionario_alunos['Media']}")
