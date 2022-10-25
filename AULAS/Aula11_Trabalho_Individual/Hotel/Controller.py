import datetime

def salvar(nome):
    with open('DataBase.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')

def fazercheckin():
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

def cpfValidator(cpf):
    CPFS = ["00000000000","11111111111", "22222222222", "33333333333", "44444444444", 
        "55555555555", "66666666666", "77777777777", "88888888888", "99999999999"]
    hasError = False
    # Limpa o cpf, retira pontos traços e tudo que não seja um número
    cpf = [int(char) for char in cpf if char.isdigit()]        

    # Verifica se o cpf são números repetidos
    if ''.join(map(str, cpf)) in CPFS:
        hasError = True

    # verifica se o tamanho está correto
    if len(cpf) != 11:
        hasError = True

    if not(hasError):
        for i in range(9, 11):
            value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != cpf[i]:
                hasError = True
    
    if hasError:
        return False
    else:
        return True


def printmenu():

    funcoes = ['1','2','3','4','5']
    poli = "-"*50
    espaco = " "*10
    espaco1 = " "*2

    print(poli)
    print(f"(1) Fazer check-In\n(2) Relatório Hospedes\n(3) Procurar Hospedes\n(4) Fazer Check-Out\n(5) Finalizar Atendimento")
    print(poli)

def wellcome ():

    
    atual = datetime.datetime.now()
    hora = atual.hour
    minutos = atual.minute
    poli = "-"*50
    espaco = " "*10
    espaco1 = " "*7


    print(f"{poli}\n{espaco1}SEJA BEM VINDO NO HOTEL TRANSILVÂNIA \n{poli}")
    if hora < 12:
        print(f"{espaco}Bom dia! Horário atual: {hora} horas e {minutos} minutos.{espaco}".center(50,"="))
    elif hora < 18:
        print(f"{espaco}Boa tarde! Horário atual: {hora} horas e {minutos} minutos.{espaco}".center(50,"="))
    else:
        print(f"{espaco}Boa noite! Horário atual: {hora} horas e {minutos} minutos.{espaco}".center(50,"="))

def fazercheckout():
    print('Abra o arquivo Database.txt e delete manualmente seu relaxado!')

def listar():
    nomes = []
    with open('DataBase.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)
            print(name)



