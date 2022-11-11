#Primeiro encapsulamento é o namespace ou seja o nome do documento (conta.py)
#O segundo encapsulamento é a classe(OBJ)
class Conta:

    #Terceiro encapsulamento é o metodo construtor e seus atributos:
    def __init__ (self, titular, numero, saldo, limite):

        #Variáveis Objeto acessando os atributos das classes
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    #pass

    #Método extrato, imprima o valor dos atributos
    def extrato(self):
        print(f'Extrato de conta\nCliente: ',Conta.titular,'\nNúmero da conta: ',Conta.numero,'\nSaldo da conta: ',Conta.saldo,'\nLimite da conta: ',Conta.limite )

    #Metodo depositar, recebe variavel objeto e atributo valor interno metodo
    def depositar(self, valor):
        #Realiza condicional de incremento ao saldo
        self.saldo += valor

    #Metodo sacar, recebe variavel objeto e atributo valor interno metodo
    def saque(self, valor):
        #realiza condicional de decremento do saldo
        self.saldo -= valor

    #Metodo transferir recebe variavel objeto e atributo valor, origem, destino internos do metodo
    def transferir(self, valor, origem, destino):
        #Recebe as condicionais de sacar e para atributo origem
        origem.sacar(valor)
        destino.depositar(valor)
def linha():
    print("*"*30)