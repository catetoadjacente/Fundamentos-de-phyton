# import tkinter as tk
# janela= tk.Tk()
# janela.geometry('600x400')



# def submit():
#     email= mail_var.get()
#     senha= senha_var.get()

#     print('email:', email)
#     print('senha:', senha)

# mail_var=tk.StringVar()
# senha_var=tk.StringVar()

# frame_dados= tk.Frame(janela, bg='lightgreen')
# frame_dados.place(relx=0.05 , rely=0.05, relheight=0.45, relwidth=0.9)

# frame_baixo= tk.Frame(janela, bg='lightgreen')
# frame_baixo.place(relx=0.05, rely=0.55, relheight=0.4, relwidth=0.9)

# label_email=  tk.Label(frame_dados, text= 'Digite seu email:', bg='lightgreen')
# label_email.place(relx=0.05, rely=0.3)

# label_senha= tk.Label(frame_dados, text='Digite sua senha:', bg="lightgreen")
# label_senha.place(relx=0.05, rely=0.5)

# entrada_mail= tk.Entry(frame_dados, textvariable=mail_var, relief='sunken', width=45)
# entrada_mail.place(relx=0.3, rely=0.3)
# entrada_senha= tk.Entry(frame_dados,textvariable=senha_var,  relief='sunken', width=45, show='*')
# entrada_senha.place(relx=0.3, rely=0.5)

# btn= tk.Button(frame_dados, text='submit', command= submit, bg='green', fg='white')
# btn.place(relx=0.3, rely=0.8, width=200, height=30)



import tkinter as tk

janela = tk.Tk()
janela.geometry('600x400')

def submit():
    email = mail_var.get()
    senha = senha_var.get()
    
    # Atualiza o texto do label em vez de apenas printar no terminal
    resultado_texto = f"E-mail: {email}\nSenha: {senha}"
    label_resultado.config(text=resultado_texto)

mail_var = tk.StringVar()
senha_var = tk.StringVar()

frame_dados = tk.Frame(janela, bg='lightgreen')
frame_dados.place(relx=0.05 , rely=0.05, relheight=0.45, relwidth=0.9)

frame_baixo = tk.Frame(janela, bg='lightgreen')
frame_baixo.place(relx=0.05, rely=0.55, relheight=0.4, relwidth=0.9)

# --- WIDGETS DO FRAME DADOS ---
label_email = tk.Label(frame_dados, text='Digite seu email:', bg='lightgreen')
label_email.place(relx=0.05, rely=0.3)

label_senha = tk.Label(frame_dados, text='Digite sua senha:', bg="lightgreen")
label_senha.place(relx=0.05, rely=0.5)

entrada_mail = tk.Entry(frame_dados, textvariable=mail_var, relief='sunken', width=45)
entrada_mail.place(relx=0.3, rely=0.3)

entrada_senha = tk.Entry(frame_dados, textvariable=senha_var, relief='sunken', width=45, show='*')
entrada_senha.place(relx=0.3, rely=0.5)

btn = tk.Button(frame_dados, text='submit', command=submit, bg='green', fg='white')
btn.place(relx=0.3, rely=0.8, width=200, height=30)

# --- NOVO: LABEL NO FRAME BAIXO ---
# Este label começa vazio e será preenchido quando clicar no botão
label_resultado = tk.Label(frame_baixo, text='', bg='lightgreen', justify='left', font=('Arial', 10, 'bold'))
label_resultado.place(relx=0.05, rely=0.1)









janela.mainloop()

