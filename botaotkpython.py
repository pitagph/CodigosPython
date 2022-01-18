from tkinter import *

def funcClicar():
    print("Botão pressionado")


Janela = Tk()

texto = Label(Janela, text = "Exemplo Botão")
texto.pack()

pic = PhotoImage(file="best-gifs-7-trippy.gif")
logo = Label(Janela, image = pic)
logo.pack()

botao = Button(Janela, text = 'Clique', command = funcClicar)
botao.pack()

Janela.mainloop()