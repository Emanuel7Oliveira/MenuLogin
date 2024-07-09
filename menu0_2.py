import tkinter as tk
from tkinter import messagebox

def senha():
    ent = e3.get()
    if ent == '123':
        messagebox.showinfo(title='Login aprovado', message=f'Bem vindo, usuário.')
    else:
        messagebox.showerror(title='Login ou senha incorretos', message='Falha na autenticação, tente novamente.')

def registro():
    nome1 = e1.get()
    sobren1 = e2.get()
    senha1 = e3.get()
    
    with open('logon.txt', 'a') as arquivo:
        arquivo.write(f"\nusuario: {nome1}\nnome completo: {nome1} {sobren1}\nsenha: {senha1}")
    
    messagebox.showinfo(title='Registro concluído', message='Sua conta foi criada com sucesso!', icon='info', detail='Já podes fazer login.')

# creating window, configure window color, window title, window size
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.funcionamento()
        self.config(bg='#900C3F')
        
    def funcionamento(self):
        # creating labels
        tk.Label(self, text='Primeiro nome', width=20, height=1, foreground='white', background='black').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self, text='Sobrenome', width=20, height=1, foreground='white', background='black').grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self, text='Senha', width=20, height=1, foreground='white', background='black').grid(row=2, column=0, padx=10, pady=10)

        # creating entry boxes
        global e1, e2, e3
        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e3 = tk.Entry(self)
        # placing entry boxes
        e1.grid(row=0, column=1, padx=10, pady=10)
        e2.grid(row=1, column=1, padx=10, pady=10)
        e3.grid(row=2, column=1, padx=10, pady=10)

        # creating buttons
        button1 = tk.Button(self, text='Sair', width=5, fg="white", bg="black", command=self.master.destroy)
        entrada = tk.Button(self, text='Criar sua conta', width=16, fg="white", bg="black", command=registro)
        # placing buttons
        button1.grid(row=3, column=1, padx=1, pady=10)
        entrada.grid(row=3, column=0, padx=10, pady=10)

root = tk.Tk()
root.title('Menu de login:')
root.geometry("700x500")
root.config(bg='#581845')

myapp = App(root)
root.mainloop()