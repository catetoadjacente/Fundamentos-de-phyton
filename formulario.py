import tkinter as tk

janela= tk.Tk()
janela.geometry('600x400')


frame_topo = tk.Frame(janela, bg="lightblue",)
frame_topo.place(relx=0.05, rely=0.05, relheight= 0.15, relwidth=0.9)


frame_meio = tk.Frame(janela, bg='lightgreen')
frame_meio.place(relx=0.05, rely=0.23, relheight=0.55, relwidth=0.9 )


frame_baixo = tk.Frame(janela, bg="yellow",)
frame_baixo.place(relx=0.05, rely=0.8, relheight= 0.15, relwidth=0.9)


palavra_topo = tk.Label(frame_topo, text='Frame superior', bg='lightblue')
palavra_topo.place(relx=0.5, rely=0.5, anchor='center')

palavra_meio= tk.Label(frame_meio, text='Frame do meio', bg='lightgreen')
palavra_meio.place(relx=0.5, rely=0.5, anchor='center')


palavra_baixo= tk.Label(frame_baixo, text= 'Frame inferior', bg= 'yellow',)
palavra_baixo.place(relx=0.5, rely=0.5, anchor='center')


janela.mainloop()
