from conta import Conta, linha

linha()
print ('       Inicio do menu') 
linha()

conta = Conta(input('Nome: '),
int(input('Conta: ')),
float(input('Saldo: ')),
float(input('Limite: ')))

linha()

print ('       Digite outros dados da conta') 
linha()

#print('O nome é {} \nA conta é {} \no saldo é {} \ne o limite de {}'.format(conta.get_titular(), conta.get_numero(), conta.get_saldo(), conta.get_limite()))







conta2 = Conta(input('Nome: '),
int(input('Conta: ')),
float(input('Saldo: ')),
float(input('Limite: ')))

linha()
print ('       Extrato da conta 1') 
linha()

print('O nome 1 é {} \nA conta é {} \no saldo é {} \ne o limite de {}'.format(conta.get_titular(), conta.get_numero(), conta.get_saldo(), conta.get_limite()))

linha()
print ('       Extrato da conta 2') 
linha()

print('O nome 2 é {} \nA conta é {} \no saldo é {} \ne o limite de {}'.format(conta2.get_titular(), conta2.get_numero(), conta2.get_saldo(), conta2.get_limite()))

