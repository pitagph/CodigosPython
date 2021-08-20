import tkinter as tk

janelaPrincipal = tk.Tk()
texto = tk.Label(janelaPrincipal,
                text = 'Minha primeira janela em Python')
texto.place(relx = 0.5, rely = 0.5, anchor = 'center')
janelaPrincipal.mainloop()