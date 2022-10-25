#import datetime
from Controller import salvar, fazercheckin, cpfValidator, printmenu, wellcome, fazercheckout, listar

while True:
    wellcome()
    printmenu()

    menu = int(input("=> "))

    match menu:

        case 1:
            fazercheckin()
            
        case 2:
            listar()
            input('Listar SAporra!')
        case 3:
            procurarhospedes() 
            
        case 4:
            fazercheckout() 

        case 5:
            print(' Não é para sair! '.center(50, "*"))
            break
            
        case _:
            print("Digite uma opção válida.\n Uma das opções do Cadastro.")
