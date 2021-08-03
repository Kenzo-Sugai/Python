def calculo(w, M, ε):
    z = [1] # Lista de números complexos
    menores = [0] # Lista da distância
    ok = [] # Lista de ok
    f = True
    for c in range(M):
        z.append(z[c]**2 + w)
    print(z)

    n = 0
    for k in range(M):
        for i in range(M):
            if abs(z[k]-z[i]) > ε:
                f = False
        ok.append(f)    

    for x in range(M):
        if ok[x] == True:
            print("O menor índice procurado é: %d" %x)
            break
        else:
            print("Não há índice a partir do qual um elemento e seus subsequentes estejam a uma distância menor que: %.2f" %ε)
            break
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