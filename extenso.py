def numero_texto(n):
    dicionario_unidades = {
        0: "zero",
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",

    }
    dicionario_dezenas = {
        0: "zero",
        1: "trocar",
        2: "vinte",
        3: "trinta",
        4: "quarenta",
        5: "cinquenta",
        6: "sessenta",
        7: "setenta",
        8: "oitenta",
        9: "noventa",

    }
    dicionario_centenas = {
        1: "cento",
        2: "duzentos",
        3: "trezentos",
        4: "quatrocentos",
        5: "quinhentos",
        6: "seiscentos",
        7: "setecentos",
        8: "oitocentos",
        9: "novecentos"
    }
    n = str(n)
    n = n[::-1]
    i = 0
    lista = []
    for numeros in n:
        numeros = int(numeros)
        if i == 0:
            lista.append(dicionario_unidades[numeros])
        if i == 1:
            lista.append(dicionario_dezenas[numeros])
        if i == 2:
            lista.append(dicionario_centenas[numeros])
        i += 1
    lista = lista[::-1]
    lista = " e ".join(lista)
    if 'e zero' in lista:
        lista = lista.replace('e zero', '')
    elif 'trocar e zero' in lista:
        lista = lista.replace('trocar e zero', 'dez')
    elif 'trocar e um' in lista:
        lista = lista.replace('trocar e um', 'onze')
    elif 'trocar e dois' in lista:
        lista = lista.replace('trocar e dois', 'doze')
    elif 'trocar e três' in lista:
        lista = lista.replace('trocar e três', 'treze')
    elif 'trocar e quatro' in lista:
        lista = lista.replace('trocar e quatro', 'quatorze')
    elif 'trocar e cinco' in lista:
        lista = lista.replace('trocar e cinco', 'quinze')
    elif 'trocar e seis' in lista:
        lista = lista.replace('trocar e seis', 'dezesseis')
    elif 'trocar e sete' in lista:
        lista = lista.replace('trocar e sete', 'dezessete')
    elif 'trocar e oito' in lista:
        lista = lista.replace('trocar e oito', 'dezoito')
    elif 'trocar e nove' in lista:
        lista = lista.replace('trocar e nove', 'dezenove')

    print(lista)

def main():
    n = int(input("Digite um número entre 0 e 999: "))
    numero_texto(n)
main()