def primos(limite):
    lista = []
    for x in range(limite+1):
        if x == 0 or x == 1:
            x = 0
            lista.append(x)
        elif x == 2 or x == 3 or x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19:
            lista.append(x)
        else:
            if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0 or x % 13 == 0 or x % 17 == 0 or x % 19 == 0:
                x = 0
                lista.append(x)
            else:
                lista.append(x)
    for x in range(limite+1):
        print("%d"% lista[x], end=" ")  
