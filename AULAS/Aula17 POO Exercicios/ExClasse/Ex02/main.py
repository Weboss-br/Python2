from carro import Carro, linha1, linha2

linha1()

carro = Carro(input('Qual a marca do carro: '),

str(input('Qual é o modelo: ')),
str(input('Categoria: ')),
str(input('Cor: ')))

linha1()

carro2 = Carro(input('Qual a marca do carro: '),

str(input('Qual é o modelo: ')),
str(input('Categoria: ')),
str(input('Cor: ')))

linha2()

print('A marca é {} \nO modelo é {} \nA categoria é {} \na cor é {}'.format(carro.marca, carro.modelo, carro.categoria, carro.cor))

linha2()

print('A marca é {} \nO modelo é {} \nA categoria é {} \na cor é {}'.format(carro2.marca, carro2.modelo, carro2.categoria, carro2.cor))
