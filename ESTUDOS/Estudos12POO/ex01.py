#Estudando Funções e funções com parâmetro.

#Função simples: 
''''
def mostraLinha():
    print('-'*35)

mostraLinha()
'''
#Função com parâmetro:

def mensagem(msg):
    print('-'*35)
    print(msg)
    print('-'*35)

mensagem('Parâmetro recebido')
mensagem(input('Escreva o parâmetro: '))