import tkinter as tk
from tkinter import *

class Table:
   def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

# take the data
lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Aaryan', 'Pune', 18),
       (3, 'Vaishnavi', 'Mumbai', 20),
       (4, 'Rachna', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)

#Ojeto Janela
JanelaIndex = tk.Tk()

#Configurações da janela
JanelaIndex.title("Janela Index - Tabela BD")
JanelaIndex.geometry("680x420")
JanelaIndex.minsize(680,420)
JanelaIndex.maxsize(680,420)
# Textos Label
texto = tk.Label(JanelaIndex, text= 'Tabela Lista Dados')
text2 = tk.Label(JanelaIndex, text= 'Janela Index')
texto.place(relx = 0.5, rely = 0.1, anchor = 'ne')
text2.place(relx = 1.0, rely = 0.0, anchor = 'ne')
#Iniciar a Janela
JanelaIndex.mainloop()