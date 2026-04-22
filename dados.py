
import tkinter as tk
janela = tk.Tk()
janela.geometry('600x400')


campo_email = tk.Entry (janela, width=40)
campo_email.pack(pady=10)

campo_senha = tk.Entry(janela, show="*")
campo_senha.pack(pady=20)
janela.mainloop()






