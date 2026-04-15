import tkinter as tk

janela = tk.Tk()
janela.title = ('Estrutura base')
janela.geometry('600x400')

frame_azul = tk.Frame(janela, bg='lightblue')
frame_azul.place(relheight=1, relwidth=0.2, relx=0, rely=0)

palavra_azul= tk.Label(frame_azul,text='frame Esquerdo', bg='lightblue')
palavra_azul.place(rely=0.2, relx=0.2)

frame_verde = tk.Frame(janela, bg ='lightgreen')
frame_verde.place(relx= 0.2, rely=0 , relwidth=0.8,  relheight=0.8)

palavra_verde = tk.Label(frame_verde, text= 'Frame direito', bg='lightgreen')
palavra_verde.place(rely=0.2, relx=0.1,)

frame_amarelo = tk.Frame(janela, bg='yellow')
frame_amarelo.place(relx=0.2, rely=0.7, relwidth=0.8, relheight=0.3)

palavra_amarelo =tk.Label(frame_amarelo, text='Frame inferior direito', bg='yellow') 
palavra_amarelo.place(relx=0.1, rely=0.2)

janela.mainloop()
