from _boas_vindas import boasvindas
from _menu import menu
from _fazer_checkin import fazercheck
from note_read_file import listar
#from _cadastro_cpf import *


boasvindas()

while True:
    

    menu = int(input("=> "))

    match menu:

        case 1:
            fazercheck()
            
        case 2:
            listar()
        
        case 3:
            procurarhospedes() 
            
        case 4:
            fazercheckout() 

        case 5:
            
            print(' Sair '.center(50, "*"))
            break
        case _:
            print("Digite uma opção válida.\n Uma das opções do Cadastro.")
