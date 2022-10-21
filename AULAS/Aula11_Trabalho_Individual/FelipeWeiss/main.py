from time import sleep
from controller import saudacao, checkin, listarHospedes,procurarHospedes,checkout, finalizar

def menu():

    saudacao()

    while True:
        try:
            print('1 - Fazer Check-In\n2 - Listar Hóspedes\n3 - Procurar Hóspedes\n4 - Fazer Check-Out\n5 - Sair\n\n')
            opcaoMenu = int(input('Digite uma das Opções: '))

            if opcaoMenu == 1:
                while True:
                    nomehospede = str(input('Qual seu nome completo? '))
                    cpfhospede = int(input('Qual seu cpf? '))
                    idadehospede = int(input('Qual sua idade? '))
                    hospede = {'Nome': nomehospede, 'CPF': cpfhospede, 'Idade': idadehospede}
                    checkin(hospede)
                    break
            
            elif opcaoMenu == 2:
                while True:
                    print(listarHospedes())
                    sleep(1)
                    print()
                    break

            elif opcaoMenu == 3:
                while True:
                    pessoa = str(input('Digite o Nome do hóspede:'))
                    procurarHospedes(pessoa)
                    break

            elif opcaoMenu == 4:
                while True:
                    pessoa = str(input('Digite o Nome do hóspede:')) 
                    checkout(pessoa)
                    break

            elif opcaoMenu == 5:
                finalizar()
                break
        except(ValueError):
            print('Opção Inválida\n')
            sleep(1)

menu()

