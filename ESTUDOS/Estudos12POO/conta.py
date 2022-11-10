
class Conta:
    numero = ''
    titular = 0
    saldo = 0
    limite = 0

    def __str__(self):
        return f'{self.titular} - {self.saldo} - {self.limite} - {self.numero}' 