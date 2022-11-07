class Computador:
    def __init__ (self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    pass

computador1 = Computador('Asus', '15gb', 'Nvidia')
computador2 = Computador('Dell', '12gb', 'GeForce')
computador3 = Computador('Acer', '10gb', 'ATM')

print(computador1.marca, computador1.memoria_ram, computador1.placa_de_video)

print(computador2.marca, computador2.memoria_ram, computador2.placa_de_video)

print(computador3.marca, computador3.memoria_ram, computador3.placa_de_video)