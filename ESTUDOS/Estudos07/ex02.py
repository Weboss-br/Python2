
#Checagem de String + estrutura de if else:
#Fonte: https://www.w3schools.com/python/python_strings.asp

txt = input('Qual o significado da vida, do universo e tudo mais? ')
validador = '42' in txt


if validador == True:
    print("Não esqueçá sua toalha!")

else:
    print("Leia mais!")