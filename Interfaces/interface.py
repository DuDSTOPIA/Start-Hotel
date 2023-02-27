
from tkinter import *
import Connection as connect


class Interfaces:
    def __init__(self, nome, nascimento, rg, cpf):
        self.nome = nome,
        self.nascimento = nascimento,
        self.rg = rg,
        self.cpf = cpf
        self.janela = Tk()
        self.janela.title('Hotel Sistem')
        self.resolucao_X = self.janela.winfo_screenwidth()
        self.resolucao_Y = self.janela.winfo_screenheight()
        self.janela.geometry(f"{int(self.resolucao_X/2)}x{int(self.resolucao_Y/2)}+{int(self.resolucao_X/2-400)}+{int(self.resolucao_Y/2-250)}")
        self.frame_Barra_ferramentas = Frame(self.janela, bg="orange", height=30, width=self.resolucao_X)
        self.frame_Barra_ferramentas.pack(side="top")
        self.janela.configure(background='lightgray')


    def Menu_Principal(self):
        texto_orientacao = Label(self.janela, bd=2, bg='lightgray', font=("calibri", 15), text="Bem Vindo")
        texto_orientacao.pack()




        self.janela.mainloop()

    def Pessoa_Fisica(self):

        texto_orientacao = Label(janela, text="insira seus dados do cadastro")
        texto_orientacao.grid(column=1, row=0)

        # Nome
        texto_nome = Label(janela, text="Nome: ")
        texto_nome.grid(column=0, row=1)
        NOME = Entry(janela, bd=2, font=("calibri", 15), justify=CENTER, width=50)
        NOME.grid(column=1, row=1)

        # Nascimento
        texto_nascimento = Label(janela, text="Nascimento: ")
        texto_nascimento.grid(column=0, row=2)
        NASCIMENTO = Entry(janela, width=10)
        NASCIMENTO.grid(column=1, row=2)

        # RG
        texto_RG = Label(janela, text="RG: ")
        texto_RG.grid(column=0, row=3)
        RG = Entry(janela, width=50)
        RG.grid(column=1, row=3)

        # CPF
        texto_CPF = Label(janela, text="CPF: ")
        texto_CPF.grid(column=0, row=4)
        CPF = Entry(janela, width=50)
        CPF.grid(column=1, row=4)

        def funcionar():
            id = 6
            nome = NOME.get()
            nascimento = NASCIMENTO.get()
            rg = RG.get()
            cpf = CPF.get()

            connect.SQL.adicionar(id, nome, nascimento, rg, cpf)

            print(id, nome, nascimento, rg, cpf)

        # Botão
        botao = Button(janela, text="adicionar", command=funcionar)
        botao.grid(column=0, row=6)

        janela.mainloop()

