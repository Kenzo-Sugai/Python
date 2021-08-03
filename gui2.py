from tkinter import *
from tkinter.ttk import *
from datetime import date, datetime

janela = Tk()
janela.title("Algoritmos")
janela.geometry("500x500")

label = Label(janela, text="00:00:00", font=("Arial Bold", 40))
label.place(relx=0.5, rely=0.4, anchor=CENTER)

label2 = Label(janela, text="00/00/00", font=("Arial Bold", 40))
label2.place(relx=0.5, rely=0.5, anchor=CENTER)

def atualiza():
    tempo = datetime.now()
    label['text'] = tempo.strftime("%H:%M:%S")
    label2['text'] = tempo.strftime("%d/%m/%Y")
    janela.after(1000, atualiza)

atualiza()
janela.mainloop()