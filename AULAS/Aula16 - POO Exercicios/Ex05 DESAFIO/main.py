
#importar as classes e funções do doc conta.py 

from conta import Conta,linha

linha()
print ('Inicio do menu') 

#atributo titular 
conta = Conta(input('Digite seu nome: '))
int(input('Qual a sua conta? '))
float(input('Digite seu saldo: '))
float(input('Digite seu limite: '))




pessoa1 = Banco('Dieter Heiss', 546546546, 1500.00, 50000.00)


Banco.extrato(pessoa1)