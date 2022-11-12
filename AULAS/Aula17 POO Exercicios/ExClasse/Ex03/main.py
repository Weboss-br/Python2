#titular, numero, saldo, limite 

from conta import Conta, linha1, linha2

linha1()

conta = Conta(input('Qual a titular: '),

str(input('Qual é o modelo: ')),
str(input('Categoria: ')),
str(input('Cor: ')))

linha1()

conta2 = Conta(input('Qual a titular da conta: '),

str(input('Qual é o modelo: ')),
str(input('Categoria: ')),
str(input('Cor: ')))

linha2()

print('A titular é {} \nO modelo é {} \nA categoria é {} \na cor é {}'.format(conta.titular, conta.numero, conta.saldo, conta.limite))

linha2()

print('A titular é {} \nO modelo é {} \nA categoria é {} \na cor é {}'.format(conta2.titular, conta2.numero, conta2.saldo, conta2.limite))
