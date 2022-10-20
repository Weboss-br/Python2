#Concatenação
#https://www.w3schools.com/python/python_strings_concatenate.asp


nome = 'Dieter'
sobrenome = 'Heiss'
nomeCompleto = (nome) + ' ' + (sobrenome)

print (nomeCompleto)
txt = ('Meu nome completo é Dieter {}')
print(txt.format(sobrenome))