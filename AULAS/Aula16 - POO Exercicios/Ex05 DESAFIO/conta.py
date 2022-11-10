
class Banco:
    def __init__ (self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    pass

    def extrato(self):
        print(f'Extrato de conta\n''Nome do cliente: ',Banco.titular,'\nNúmero da conta: ',Banco.numero,'\nSaldo da conta: ',Banco.saldo,'\nLimite da conta: ',Banco.limite )

    
    def depositar(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def transferir(self, valor, destino):
        self.saldo 
