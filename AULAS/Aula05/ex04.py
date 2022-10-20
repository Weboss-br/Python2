n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1+n2)/2

print(f'Sua média foi de {media}')

print('Parabéns você passou: 'if media >=7 else'Você não atingiu a média: ')