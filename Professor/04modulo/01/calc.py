#1 -**************procedimento***********************
def mensagem():
    print('Ola') 
#1 -**************procedimento***********************

#2 -******************funcao***********************
def mensagem2():
   return 'Ola 2'
#2 -******************funcao***********************


#3 -******************Parametros***********************
def soma(n1, n2):
   resultado = n1 + n2
   n1= n1+2
   print('n1 dentro:', n1)
   return resultado
#3 -******************Parametros***********************

#=========================================================================================================
#1 ***********procedimento***********************
mensagem()
#1 ***********procedimento***********************

#2-******************funcao***********************

msg = mensagem2()
print(msg)
print(mensagem2())

#2-******************funcao***********************


#argumentos
n1=10
n2=20

print(soma(n1,n2))

#3-******************Parametros***********************
print('n1 fora: ', n1)
#3-******************Parametros***********************
