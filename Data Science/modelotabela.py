from tkinter import *
from tabeladb import *
class Table:
   def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
q1 = """SELECT * FROM produto;"""
lst = read_query(conexao, q1)
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])