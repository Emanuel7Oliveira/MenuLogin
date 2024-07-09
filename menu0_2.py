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
    
    with open('test.txt', 'a') as arquivo:
        arquivo.write(f"\nusuario: {nome1}\nnome completo: {nome1} {sobren1}\nsenha: {senha1}")
    
    messagebox.showinfo(title='Registro concluído', message='Sua conta foi criada com sucesso!')

# creating window, configure window color, window title, window size
j1 = tk.Tk()
j1.title('Menu de login:')
j1['background'] = 'darkblue'
j1.geometry("500x500")

# creating labels
tk.Label(j1, text='Primeiro nome', width=20, height=1, foreground='white', background='black').grid(row=0, column=0, padx=10, pady=10)
tk.Label(j1, text='Sobrenome', width=10, foreground='white', background='black').grid(row=1, column=0, padx=10, pady=10)
tk.Label(j1, text='Senha', width=10, foreground='white', background='black').grid(row=2, column=0, padx=10, pady=10)

# creating entry boxes
e1 = tk.Entry(j1)
e2 = tk.Entry(j1)
e3 = tk.Entry(j1)

# placing entry boxes
e1.grid(row=0, column=1, padx=10, pady=10)
e2.grid(row=1, column=1, padx=10, pady=10)
e3.grid(row=2, column=1, padx=10, pady=10)

# creating buttons
button1 = tk.Button(j1, text='Sair', width=5, fg="white", bg="black", command=j1.destroy)
entrada = tk.Button(j1, text='Criar sua conta', width=16, fg="white", bg="black", command=registro)

# placing buttons
button1.grid(row=3, column=1, padx=10, pady=10)
entrada.grid(row=3, column=0, padx=10, pady=10)

# running the window
j1.mainloop()