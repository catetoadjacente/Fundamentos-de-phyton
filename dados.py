
'''import tkinter as tk
janela = tk.Tk()
janela.geometry('600x400')


campo_email = tk.Entry (janela, width=40)
campo_email.pack(pady=10)

campo_senha = tk.Entry(janela, show="*")
campo_senha.pack(pady=20)
janela.mainloop()'''

import tkinter as tk
janela = tk.Tk()
janela.geometry('600x400')

texto =tk.Label(janela, text='Olá, Mundo!')
texto.pack()
frame = tk.Frame(janela, bg='lightblue')
frame.place(relheight=1, relwidth=1)
label = tk.Label(frame, text="Olá mundo", fg="Black", bg='lightblue')
label.place(relx=0.45, rely=0)
janela.title("Olá, Mundo!")
janela.mainloop()






