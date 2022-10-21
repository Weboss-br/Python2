import datetime
atual = datetime.datetime.now()
hora = atual.hour
minutos = atual.minute
poli = "-"*50
espaco = " "*10
espaco1 = " "*7

def boasvindas ():

    print(f"{poli}\n{espaco1}SEJA BEM VINDO NO HOTEL TRANSILVÂNIA \n{poli}")
    if hora < 12:
        print(f"{espaco}Bom dia! Horário atual: {hora} horas e {minutos} minutos.{espaco}".center(50,"="))
    elif hora < 18:
        print(f"{espaco}Boa tarde! Horário atual: {hora} horas e {minutos} minutos.{espaco}".center(50,"="))
    else:
        print(f"{espaco}Boa noite! Horário atual: {hora} horas e {minutos} minutos.{espaco}".center(50,"="))