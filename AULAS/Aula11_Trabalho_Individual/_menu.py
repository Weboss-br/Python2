from fazer_checkin import fazercheck
from relatorio_hospedes import relatoriohospedes
from procurar_hospedes import procurarhospedes
from fazer_checkout import fazercheckout

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
        if not(opcao in funcoes):
            print("Digite uma opção válida.\n Uma das opções do Cadastro.")
        elif opcao == '1':
            fazercheck()
            #break

        elif opcao == '2':
            relatoriohospedes() 
            #break

        elif opcao == '3':
            procurarhospedes() 
            #break

        elif opcao == "4":
            fazercheckout() 
            #break

        elif opcao == '5':
            #5 -> Finalizar Atendimento
            print(' Sair '.center(50, "*"))
            break