from controller import somaSalario

def menu():
    print('='*15, 'CALCULADORA DE SALARIO', '='*15)

    var = 'sim'
    while var == 'sim':
        n1 = float(input('Digite seu primeiro salario: '))
        n2 = float(input('Digite seu segundo salario: '))
        n3 = float(input('Digite seu terceiro salario: '))
        n4 = float(input('Digite seu quarto salario: '))

        resultado = somaSalario(n1,n2,n3,n4)
        print('A soma dos salarios é: {:.2f}'.format(resultado))

        var = input ('Você deseja continuar \nSim \nNão')

menu()
print('Vc saiu do programa')