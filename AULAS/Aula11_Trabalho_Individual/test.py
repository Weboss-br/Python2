
CPFS = ["00000000000","11111111111", "22222222222", "33333333333", "44444444444", 
        "55555555555", "66666666666", "77777777777", "88888888888", "99999999999"]
#Função CPF VALIDA:

def cpfValidator(cpf):
    hasError = False
    # Limpa o cpf, retira pontos traços e tudo que não seja um número
    cpf = [int(char) for char in varcpf if char.isdigit()]        

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
       # hospedes.append(dados) 
        break