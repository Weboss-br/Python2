def salvar (nome):
    with open('txt.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')

def listar():
    nomes = []
    with open('txt.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)

    return nomes
print('Listar Nomes', listar())
salvar('João de Deus')