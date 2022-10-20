from time import sleep
import string



#Cria uma lista livros. Ela vai receber os valores/dados do livro.
livros = []

poli = '='*5
espaco = ' '*21
print(f'{espaco}Inicio do programa:{espaco}')

while True:
    print(f'{espaco}MENU DA LIVRARIA{espaco}')
    print('(1) Cadastro de Livros\n(2) Lista de Livros\n(3) Excluir Livros\n(4) Sair')
    print(poli)
    opcao = input('=>')

    if not (opcao.isnumeric()):
        print('Letras não são válidas para essa opção.')
    elif opcao == '1':
        str(input(''))
        #Título, editora, autor, genero, ano
        f