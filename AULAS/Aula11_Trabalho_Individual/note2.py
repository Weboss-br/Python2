def listar():
    nomes = []
    with open('bancodedados.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)
    return nomes
print('Listar Nomes', listar())
