#Estrutura de decisão

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1+n2)/2

print(media)

if media >= 7:
    print('Você passou de ano.')
else:
    print('Você não passou de ano.')