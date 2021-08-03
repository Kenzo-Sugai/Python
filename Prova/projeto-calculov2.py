def calculo(w, M, ε):
    z = [0] # Lista de números complexos
    ok = [] # Lista de ok
    f = False
    n = 0
    for c in range(M):
        z.append(z[c]**2 + w)

    for k in range(M):
        aux = k+1
        menores = [] # Lista da distância
        for i in range(M - k): 
            if abs(z[k] - z[aux]) < ε:
                menores.append(True)
            else:
                menores.append(False)
            aux +=1
        ok.append(menores)

    for i in range(len(ok)):
        if all(ok[i]):
            print("O menor índice procurado é: %d"% i)
            break
        if ok[i] == ok[M-1]:
            print("Não há índice a partir do qual um elemento e seus subsequentes estejam a uma distância menor que: {0}".format(ε))
        

def nomes():
    print("""
    Integrantes:

    Nome: Deverlyn Christine Gonçalves Cardoso
    RA: 22121099-0

    Nome: Kenzo Sugai
    RA: 22121005-7

    Nome: Thiago Francino Silva
    RA: 22121135-2  
    """)

def main():
    nomes()
    w = complex(input('Digite w: ')) # Inserir número complexo
    M = int(input('Digite M: ')) # Inserir limite da sequência
    ε = float(input('Digite um valor maior que zero para ε: ')) # Inserir menor valor
    calculo(w, M, ε)
main()



