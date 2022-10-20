x = "var Global"

def myfunc():
# Para fazer a var virar global, basta add global:
  #global x
  x = "Var da função"
  print("Essa é a var da função, e só! " + x)

myfunc()

print("Essa é a var Global: " + x)