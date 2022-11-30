import psycopg2

try: 
    conn = psycopg2.connect(host = "localhost", port = "5435", database = "postgres", user="teste", password = "123456")
    print('Foi')
except:
    print('Nao foi')

if conn:
    print("Sua conexão está estável.")

    cursor = conn.cursor()

    #cursor.execute("CREATE TABLE Dieter (id serial PRIMARY KEY, nome VARCHAR(15), sobreNome VARCHAR(15));")

    print("Tabela Criada")
    conn.commit()
    cursor.close()
    conn.close()