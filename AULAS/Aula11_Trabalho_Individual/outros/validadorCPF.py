


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
