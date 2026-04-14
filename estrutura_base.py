import tkinter as tk

janela = tk.Tk()
janela.title = ('Estrutura base')
janela.geometry('600x400')

frame_azul = tk.Frame(janela, bg='lightblue', width=200, height=600)
frame_azul.place(relheight=1, relwidth=0.25)
palavra_azul= tk.Label(frame_azul,text='frame Esquerdo', bg='lightblue')
palavra_azul.place(y=20, x=30)
janela.mainloop()


