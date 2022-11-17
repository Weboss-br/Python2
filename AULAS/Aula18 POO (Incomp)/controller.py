from model import Conta

def create(conta):
    contas = open('conta.txt', 'a')
    contas.write(str(conta)+'\n')
    contas.close

def read(conta):
    #Listas vazias 
    lista_contas = []
    contas = open('conta.txt', 'r')

    for conta in contas:
        conta = conta.strip()

        conta__conta = conta.split(';')

        print(conta__objeto)

        conta = Conta()
        conta.titular = conta__objeto[0]
        conta.numero = conta__objeto[1]
        conta.saldo = conta__objeto[2]

        lista_contas.append(conta)
    contas.close
    return