from conta import Conta
from controller import create, read

def menu():

    print("="*30, "Banco do Brazolia", "="*30)
    
    menu = 1
    while(menu != 0):
        menu = int(input("\n1.Criar Conta: \n2.Estatisticas da Conta: \n3.Sair: \nDigite a opção:"))
        match menu:

            case 1:
                conta = Conta()

                conta.titular=str(input("Nome: "))
                conta.numero=int(input("Número: "))
                conta.saldo=float(input("Saldo: "))
                create(conta)

            case 2:
                
                lista_contas = read()
                #print(lista_contas)
                #print("="*30)
                for c in lista_contas:
                    print(c)

            case _:
                print("Close")
                break


menu()