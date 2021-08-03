def texto(palavras):
    ABC = palavras.replace("-", " ")
    separar = ABC.split()
    ordenar = sorted(separar)
    total = ""
    ia = 0
    ib = 0
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alfabeto2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ó', 'ã', 'ê', 'á', 'ç']
    for x in range(len(ordenar)):
        if ordenar[x] == ordenar[-1]:
            total = total+ordenar[x]
        else:
            total = total+ordenar[x]+"-"
    for x in total:
        for y in range(31):
            if y < 26:
                if x == alfabeto[y]:
                    ia += 1
            if y < 32:
                if x == alfabeto2[y]:
                    ib += 1
    print(total)
    print("Maiúsculas = %d"% ia)
    print("Minúsculas = %d"% ib)