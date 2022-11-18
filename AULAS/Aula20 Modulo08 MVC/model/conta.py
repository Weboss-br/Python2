class Conta:
    __agencia = 'Agencia de Brazolia'
    __numero_agencia = 0

    @property #getter
    def agencia(self):
        return self.agencia
    @agencia.setter #setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property #getter
    def numero_agencia(self):
        return self.numero_agencia
    @numero_agencia.setter #setter
    def numero_agencia(self, numero_agencia):
        self.__numero_agencia = numero_agencia

    def __str__(self):
        return f'{self.agencia}; {self.numero_agencia}'