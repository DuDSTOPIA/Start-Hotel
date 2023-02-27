

class Interface_Feature:

    def Botoes(self, frame, texto, comando, packconf):
        botao = Button(frame, text=texto, command=comando)
        botao.pack(packconf)