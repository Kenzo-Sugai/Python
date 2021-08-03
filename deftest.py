
def quadrado(a=1,b=1,c=1,d=1,e=1,f=1,g=1):
    lista = [int(a), int(b), int(c), int(d), int(e), int(f), int(g)]
    for x in range(7):
        mult = lista[x]*lista[x]
        lista[x] = mult
    return print([mult])

print(quadrado(1, 2, 3, 4, 5, 6, 7))

