def fazercheck():
    print('Fazer Check-In')
    
    nome = (input('Digite o nome: '))
    def salvar (nome):
        with open('bancodedados.txt', 'a') as arquivo:
            arquivo.write(f'{nome}\n')

    salvar(nome)