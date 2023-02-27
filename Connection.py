

import pyodbc

class SQL:

    def adicionar(id, nome, nasc, rg, cpf):
        dados_conexao = (
            "Driver={SQL Server};"
            "Server=DESKTOP-NA4VUNH;"
            "Database=CLIENTE"
        )

        conexao = pyodbc.connect(dados_conexao)

        print("Conexao bem sussedida")

        cursor = conexao.cursor()

        comando = f"""INSERT INTO CADASTRO_FISICO(id, nome, nasc, rg, cpf)
        VALUES
            ({id}, '{nome}', '{nasc}', '{rg}', {cpf})"""

        cursor.execute(comando)
        cursor.commit()