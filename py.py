def quadrado(a, b, c, d, e, f, g):
    lista = [a, b, c, d, e, f, g]
    for x in range(7):
        novalista = lista[x]*lista[x]
        lista.insert(novalista, lista[x])

print(quadrado(1, 2, 3, 4, 5, 6, 7))