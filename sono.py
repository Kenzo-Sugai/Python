import math

nome = str(input("Qual é o seu nome? ")) # Nome
idade = int(input("Qual a sua idade? ")) # Idade
Hd = int(input("Quantas horas %s dormiu esta noite? "% nome)) # Horas dormidas

if idade < 13:
    Sono_do_nome = (Hd - 10)
if idade in range(14, 17):
    Sono_do_nome = (Hd - 9)
if idade in range(18, 64):
    Sono_do_nome = (Hd - 8)
if idade >= 65:
    Sono_do_nome = (Hd - 7)

if Sono_do_nome < 0:
    print("{0} está com {1} horas de sono a menos do que deveria".format(nome,Sono_do_nome))

else:
    print("{0} está com {1} horas de sono a mais, parabéns".format(nome,Sono_do_nome))