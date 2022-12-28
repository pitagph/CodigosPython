import tkinter as tk
import tabeladb as tadb
from modelotabela import *
from tkinter import *
import pandas as pd
# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# =================== area de procedimentos e funções do Sistema =====================================
def janelaprincipal():
    janela = tk.Tk()
    t = Table(janela)
    janela.geometry("680x420")
    texto = tk.Label(janela, text='Tabela Lista Dados')
    text2 = tk.Label(janela, text='Janela Index')
    texto.place(relx=0.5, rely=0.1, anchor='ne')
    text2.place(relx=1.0, rely=0.0, anchor='ne')

    janela.mainloop()
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PhillipeSilva')
# =============== area de Inicialização do Sistema =======================
print("Tabela de Produtos")
print("Id ======= Nome do Produto ========== Desc do Produto")
from_db = tadb.listardados()
janelaprincipal()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
