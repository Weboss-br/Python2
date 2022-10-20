
#Como ler a quantidade de digitos com len + estrutura de if else:
#Fonte: https://www.w3schools.com/python/python_strings.asp

txt = input('Escreva que eu vou contar quantos caracteres vc digitou: ')
if len(txt) == 1:
    print('É:', (len(txt)), 'caracter.')
else:
    print('São:', (len(txt)), 'caracteres.')