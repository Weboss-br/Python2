from netflix import Cliente

cliente = Cliente('Dieter', 'weboss@gmail.com', 'basic')
cliente2 = Cliente('Dieter', 'weboss@gmail.com', 'premium')



print(cliente2.plano)
cliente2.ver_filme('HarryPotter', 'premium')

cliente2.mudar_plano('basi2c')

print(cliente2.plano)
