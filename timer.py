import tkinter as tk
janela = tk.Tk()
janela.geometry('400x400')
janela.title('Timer')

frame_de_cima = tk.Frame(janela, bg='lightyellow')
frame_de_cima.place(relx=0.05, rely=0.05, relheight=0.45, relwidth=0.9)

start= tk.Button(janela, text='iniciar')


janela.mainloop()