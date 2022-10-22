from fazer_checkin import *
from relatorio_hospedes import relatoriohospedes
from procurar_hospedes import procurarhospedes
from fazer_checkout import fazercheckout
from cadastro_cpf import cpfValidator

funcoes = ['1','2','3','4','5']
poli = "-"*50
espaco = " "*10
espaco1 = " "*2

def menu():

    while True:
        print(poli)
        print(f"(1) Fazer check-In\n(2) Relatório Hospedes\n(3) Procurar Hospedes\n(4) Fazer Check-Out\n(5) Finalizar Atendimento")
        print(poli)
        opcao = input("=> ")

        match menu:

       
            case 1:
                fazercheck()
                #break

            case 2:
                relatoriohospedes() 
                #break

            case 3:
                procurarhospedes() 
                #break

            case 4:
                fazercheckout() 
                #break

            case 5:
                #5 -> Finalizar Atendimento
                print(' Sair '.center(50, "*"))
                break
            case _:
                print("Digite uma opção válida.\n Uma das opções do Cadastro.")


    varnome = input('Nome Completo: ').title()
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
        
        def salvar(dados):
            with open('bancodedados.txt', 'a') as arquivo:
                arquivo.write(f'{dados}\n')
        salvar(dados)


       # hospedes.append(dados) 
        break