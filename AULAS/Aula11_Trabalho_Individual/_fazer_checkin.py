from _cadastro_cpf import cpfValidator

def salvar(dados):
    with open('bancodedados.txt', 'a') as arquivo:
        arquivo.write(f'\n{dados}')

def fazercheck():
    print('Fazer Check-In')
    
    varnome = (input('Digite o nome: '))
    
    while True:
        vartelefone = input('Telefone com DDD: ')
        if not(vartelefone.isnumeric()):

            print('Somente números!')
        else:
            break

    while True:
        varcpf = input('CPF: ')
        #print(cpfValidator(varcpf))
       
        if cpfValidator(varcpf) != True:
            print(f"CPF inválido, digite certo.".center(50,"="))
        else: 
            print(f"Hospede cadastrado com sucesso".center(50,"="))
            dados = {
                'nome': varnome, 
                'cpf': varcpf,
                'telefone': vartelefone
            }
            
            salvar(dados)
        break


#fazercheck()

#print('Cadastrou')

def listar():
    nomes = []
    with open('bancodedados.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)
    return nomes
print('Listar Nomes', listar())
