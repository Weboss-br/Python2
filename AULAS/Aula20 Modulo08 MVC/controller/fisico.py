from model.pessoaFisica import PessoaFisica


def create_psf(conta):
    contas = open('pessoafisica.txt', 'a')
    contas.write(str(conta)+'\n')
    contas.close()

def read_psf():
    lista_contas = []
    contas = open('pessoafisica.txt', 'r')

    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(';')
        print(conta_objeto)
        
        pessoaFisica = PessoaFisica()

        pessoaFisica.agencia = conta_objeto[0]
        pessoaFisica.numero_agencia = conta_objeto[1]

        pessoaFisica.titular = conta_objeto[2]
        pessoaFisica.cpf = conta_objeto[3]
        pessoaFisica.saldo_inicial = conta_objeto[4]
        pessoaFisica.segundo_titular = conta_objeto[5]

    lista_contas.append(conta)
    contas.close()




def update_psf(conta_update:PessoaFisica): #no exercício está Conta
    lista_contas = []
    contas = open('pessoafisica.txt', 'r')

    for conta in contas:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(';')
        
        print('entrando')
        if int(conta_update.cpf) == int(conta_objeto[3]):
            print('entrou')
            lista_contas.append(str(conta_update)+'\n')
        
        else:
            lista_contas.append(conta)
    contas.close()
    contas = open('pessoafisica.txt', 'w')
    contas.writelines(lista_contas)
    contas.close()
    

def delete_psf(numero_conta):
    lista_contas = []
    contas = open('pessoafisica.txt', 'r')
    for conta in contas:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(';')
        if numero_conta != int(conta_objeto[1]):
            lista_contas.append(conta)
    
    contas.close()
    contas = open('contas.txt', 'w')
    contas.writelines(lista_contas)
    contas.close()