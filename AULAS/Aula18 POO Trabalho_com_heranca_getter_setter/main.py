from pessoafisica import PessoaFisica
from pessoajuridica import PessoaJuridica

pessoafisica = PessoaFisica("Dieter Heiss", "0036656454", 5000)
pessoajuridica = PessoaJuridica("Heiss Com. Rep.", "00073911000149", 10000)

segundotitular = pessoafisica.segundo_titular = "negrao"
segundotitular02 = pessoajuridica.segundo_titular = "branquelo"

print("*"*30, "Menu Pessoa Fisica", "*"*30)

print(f"o nome do titular é {pessoafisica.titular} eo cpf {pessoafisica.cpf} e conta com um saldo de {pessoafisica.saldo_inicial}\n ")
print("o segundo titular é:> ", segundotitular)

print("*"*30, "Menu Pessoa Juridica", "*"*30)

print(f"o nome do titular é {pessoajuridica.titular} eo cnpj {pessoajuridica.cnpj} e conta com um saldo de {pessoajuridica.saldo_inicial}")
print("o segundo titular é:> ", segundotitular02)