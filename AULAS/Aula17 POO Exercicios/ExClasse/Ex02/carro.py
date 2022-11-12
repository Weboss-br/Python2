#marca, modelo categoria cor, 
class Carro:
    def __init__ (self, marca, modelo, categoria, cor):
        self.__marca = marca
        self.__modelo = modelo
        self.__categoria = categoria
        self.__cor = cor
        #lista_cores = ['Azul', 'Amarelo', 'Verde', 'Vermelho', 'Branco', 'Preto']
        #if self.__cor in lista_cores:
        #    self.__cor = cor
        #else:
        #    print('Cor não cadastrada')

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self,modelo):
        self.__modelo = modelo

    @property
    def categoria(self):
        return self.__categoria
    @categoria.setter
    def categoria(self,categoria):
        self.__categoria = categoria

    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def set_cor(self,cor):
        self.__cor = cor
    
    def __str__(self):
        return f'Espécie:{self.marca}\nRaça:{self.modelo}\ncategoria:{self.categoria}\nCor:{self.cor}'

def linha1():
    print("*"*30, 'Lista de carros', "*"*30)

def linha2():
    print("*"*30, 'Resultado de carros', "*"*30)