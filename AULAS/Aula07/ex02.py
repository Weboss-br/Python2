#Dicionário com input
carro = str(input('Digite seu carro: '))
ano = int(input('Digite o ano de fabricação: '))
cor = str(input('Cor do carro: '))
pais = str(input('Local de fabricação: '))

dicionario = {
    'Carro': carro, 
    'anoFabricacao': ano,
    'cor': cor,
    'fabricacao:': pais,
    }
print('\n')
print(dicionario,'\n')
print(dicionario['cor'])