class Pessoas:
    nome = '0'
    cpf = '0'
    idade = '0'

    def __str__(self):
        return f'{self.nome} - {self.cpf} - {self.idade}'