import tkinter as tk
janela= tk.Tk()
janela.geometry('600x400')

tela= tk.Frame(janela, bg= "teal")
tela.place(relwidth=1, relheight=1)

b_vindo= tk.Label(janela, text='Bem Vindo', bg= 'teal', font=("Arial", 20, "bold"))
b_vindo.pack(pady=30)

nome= tk.Label(janela, 'Digite seu nome', bg= 'teal', font=("Arial", 20, "bold"))
nome.place(relx=0, rely=0.2)




'''nome= tk.Entry(janela, relief='sunken')'''

janela.mainloop()