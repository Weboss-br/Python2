from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica

from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf

def menu():

    menu = 1
    while(menu != 0):
        print("="*30, "Banco do Brazolia", "="*30)

        menu_inicial = int(input("\n1.Pessoa Física \n2.Pessoa Jurídica \nEscolha: "))

        match menu_inicial:

            case 1: #pessoaFísica
                menu = int(input("\n1.Criar Conta PF: \n2.Listar Conta PF: \nDigite a opção:"))
                match menu:
                    case 1: #Criar

                        pessoaFisica = PessoaFisica()

                        pessoaFisica.titular = input("Titular: ")
                        pessoaFisica.cpf = input("Número: ")
                        pessoaFisica.saldo_inicial = input("Saldo: ")
                        
                        print("Deseja Cadastrar um Segundo Titular: \n")
                        v= input('sim ou nao: ')

                        if v=='sim':
                            pessoaFisica.segundo_titular = input("Digite o Nome do 2° Titular: ")
                            
                        create_psf(pessoaFisica)


                    case 2: # Listar
                        read_psf()

            case 2: #pessoaJuridica
                menu = int(input("\n1.Criar Conta PJ: \n2.Listar Conta PJ: \nDigite a opção:"))
                match menu:
                    case 1: # Criar PJ
                        conta = PessoaJuridica()

                        conta.titular=str(input("Titular: "))
                        
                        conta.cpf=int(input("Número: "))
                        conta.saldo_inicial=float(input("Saldo: "))
                        
                        print("Deseja Cadastrar um Segundo Titular: \n")
                        valor=str(input('Digite: sim ou nao.'))
                        if valor=='sim':
                            conta.segundo_titular = str(input("digite o nome do 2° titular: "))
                        create_pj(conta)
                    case 2: # Listar
                        read_pj()