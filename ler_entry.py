import tkinter as tk
janela= tk.Tk()
janela.geometry('600x400')

frame_dados= tk.Frame(janela, bg='lightgreen')
frame_dados.place(relx=0.05 , rely=0.05, relheight=0.5, relwidth=0.9)

frame_baixo= tk.Frame(janela, bg='lightgreen')
frame_baixo.place(relx=0.05, rely=0.58, relheight=0.4, relwidth=0.9)
label_email=  tk.Label(frame_dados, text= 'digite seu email:', bg='lightgreen')
label_email.place(relx=0.05, rely=0.3)
ler



janela.mainloop()

