class Animais:
    especie = '0'
    cor = '0'
    raca = '0'

    def __str__(self):
        return f'{self.especie} - {self.cor} - {self.raca}'