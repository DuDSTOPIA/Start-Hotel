import pyodbc
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-NA4VUNH;"
    "Database=CLIENTE"
)
id = 5
nome = 'JULHO'
nasc = '05/10/1999'
rg = '12345678'
cpf = 11122233344
conexao = pyodbc.connect(dados_conexao)

print("Conexao bem sussedida")

cursor = conexao.cursor()

comando = f"""INSERT INTO CADASTRO_FISICO(id, nome, nasc, rg, cpf)
VALUES
    ({id}, '{nome}', '{nasc}', '{rg}', {cpf})"""

cursor.execute(comando)
cursor.commit()