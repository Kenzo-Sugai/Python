from tkinter import *
from tkinter import scrolledtext

janela = Tk()
janela.title("Filtro de Palavras")
janela.geometry("800x800")

txt = scrolledtext.ScrolledText(janela, width=50, height=28)
txt.place(relx=0.5, rely=0.6, anchor=CENTER)

Palavrasuspeita = Label(janela, text='Palavra suspeita:', font=("Arial", 14))
Palavrasuspeita.place(relx=0.2, rely=0.05, anchor=E)

Frequencia = Label(janela, text='Frequência:', font=("Arial", 14))
Frequencia.place(relx=0.2, rely=0.1, anchor=E)

Ocorrencias = Label(janela, text="Ocorrências", font=("Arial", 14))
Ocorrencias.place(relx=0.2, rely=0.25, anchor=E)

entrada1 = Entry(janela, width=15, font=("Arial", 14))
entrada1.place(relx=0.45, rely=0.05, anchor=E)

entrada2 = Entry(janela, width=15, font=("Arial", 14))
entrada2.place(relx=0.45, rely=0.1, anchor=E)

def encontrarpalavras():
    txt.delete(0.1, END)
    entrada2.delete(0,END)
    palavra = entrada1.get()
    i = 0
    arquivo = open("chat.txt", "r")
    for line in arquivo:
        line.strip().split('\n')
        if palavra in line:
            i += 1
            txt.insert(INSERT, line+'\n')
    entrada2.insert(0, i)
    arquivo.close()

botao = Button(janela, text="Pesquisar!", command=encontrarpalavras)
botao.place(relx=0.6, rely=0.05, anchor=E)

janela.mainloop()