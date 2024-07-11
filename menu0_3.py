import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *


# My func of register login(Already working on)
def registro():
    nome1 = e1.get()
    sobren1 = e2.get()
    senha1 = e3.get()
    idade = combo.get()
    if senha1 == "" or sobren1 == "" or nome1 == "":
        messagebox.showerror(title="Erro ao criar login!", message='Falha ao criar conta\nTente novamente.')
    else:
        with open('logon.txt', 'a') as arquivo:
            arquivo.write(f'\nusuario: {nome1}\nnome completo: {nome1} {sobren1}\nsenha: {senha1}\nIdade:{idade}')
        arquivo.close()
        messagebox.showinfo(title='Registro concluído', message='Sua conta foi criada com sucesso!', icon='info', detail='Já podes fazer login.')

# Creating frame inside window, configuring color, title and size
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, columnspan=1)
        self.funcionamento()
        self.config(width=300, height=300, bg='#a3483d')
        self.frames()
        
        
    def frames(self):
         global combo
         frame_1 = tk.Frame(self, width=350, height=120,bg='#999999')
         frame_1.grid(row=0,rowspan=2, column=2)
         tk.Label(frame_1, text='Selecione sua idade', width=20, height=1, foreground='white', background='black').grid(row=0, column=2)
         combo = Combobox(frame_1, width=10)
         combo["values"]= [" ", "14-17", "18-24", "25-34", "35+"]
         combo.current(0)
         combo.grid(row=1, column=2, padx=1, pady=10)
        
         
    def funcionamento(self):
        tk.Label(self, text='Primeiro nome', width=20, height=1, foreground='white', background='black').grid(row=0, column=0, columnspan=1, padx=10, pady=10)
        tk.Label(self, text='Sobrenome', width=20, height=1, foreground='white', background='black').grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self, text='Senha', width=20, height=1, foreground='white', background='black').grid(row=2, column=0, padx=10, pady=10)
        
        # creating entry boxes
        global e1, e2, e3
        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e3 = tk.Entry(self, show='*')
        # placing entry boxes
        e1.grid(row=0, column=1, padx=10, pady=10)
        e2.grid(row=1, column=1, padx=10, pady=10)
        e3.grid(row=2, column=1, padx=10, pady=10)
        
        # creating buttons
        button1 = tk.Button(self, text='Sair', width=5, fg="white", bg="black", command=self.master.destroy)
        entrada = tk.Button(self, text='Criar sua conta', width=16, fg="white", bg="black", command=registro)
        # placing buttons
        entrada.grid(row=3, column=1, padx=1, pady=10)
        button1.grid(row=3, column=2, pady=10)
        

# Creating and configuring window
root = tk.Tk()
root.title('Menu de login:')
root.geometry("1200x500")
root.config(bg='#a3483d')

# Making magic work
myapp = App(root)
root.mainloop()