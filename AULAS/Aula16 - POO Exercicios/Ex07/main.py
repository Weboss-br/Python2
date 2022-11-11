from pessoa import Pessoa, linha

linha()
print ('       Inicio do menu das pessoas') 
linha()
#nome, cpf, idade, altura
pessoa = Pessoa(input('Nome: '),
int(input('CPF: ')),
float(input('Idade: ')),
float(input('Altura: ')))

pessoa2 = Pessoa(input('Nome: '),
int(input('CPF: ')),
float(input('Idade: ')),
float(input('Altura: ')))

linha()
print ('       Extrato da pessoa') 
linha()

print('O nome é {} \nA conta é {} \no saldo é {} \ne o limite de {}'.format(pessoa.get_nome(), pessoa.get_cpf(), pessoa.get_idade(), pessoa.get_altura()))

linha()
print ('       Extrato da pessoa') 
linha()

print('O nome é {} \nA conta é {} \no saldo é {} \ne o limite de {}'.format(pessoa2.get_nome(), pessoa2.get_cpf(), pessoa2.get_idade(), pessoa2.get_altura()))