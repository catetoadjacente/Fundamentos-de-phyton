import tkinter as tk
janela= tk.Tk()
janela.geometry('600x400')


frame_azul = tk.Frame(janela, bg='lightblue')
frame_azul.place(relx=0, rely=0, relheight=1, relwidth=0.2,)

palavra_azul= tk.Label(frame_azul,text='Explorador', bg='lightblue')
palavra_azul.place(relx=0.3, rely=0.2)



frame_verde_escuro= tk.Frame(janela, bg='green')
frame_verde_escuro.place(relx=0.2, rely=0., relheight=0.1, relwidth=0.8)

palavra_verde_escuro= tk.Label(frame_verde_escuro,text='pagina de codigo', bg='green', fg='white')
palavra_verde_escuro.place(relx=0.2, rely=0.2)


frame_verde = tk.Frame(janela, bg='lightgreen')
frame_verde.place(relx=0.2, rely=0.1, relheight=0.7, relwidth=0.8)

palavra_verde= tk.Label(frame_verde, text='editor de codigo', bg='lightgreen')
palavra_verde.place(relx=0.1, rely=0.2)

frame_amarelo= tk.Frame(janela, bg='yellow')
frame_amarelo.place(relx=0.2, rely=0.8, relheight=0.3, relwidth=0.8 )


palavra_amarelo= tk.Label(frame_amarelo, text='terminal', bg='yellow')
palavra_amarelo.place(relx=0.1, rely=0.2)






janela.mainloop()