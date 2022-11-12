from animal import Animal, linha1, linha2

linha1()
#especie, raca, porte, cor
animal = Animal(input('Qual a espécie do animal: '),

str(input('Qual é a raça: ')),
str(input('Porte: ')),
str(input('Cor: ')))

linha2()

print('O nome é {} \nA conta é {} \no saldo é {} \ne o limite de {}'.format(animal.especie, animal.raca, animal.porte, animal.cor))
