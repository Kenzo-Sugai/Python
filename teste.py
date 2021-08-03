from random import randint

somatoria = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
}

def lançar():
    a = randint(1, 6)
    b = randint(1, 6)
    somatoria[a + b] = somatoria[a + b] + 1

def main():
    lançamentos = 1000
    for x in range(lançamentos):
        lançar()
    for chave, valor in somatoria.items():
        print("%d = %d: %.2f%%"% (chave, valor, (valor*100/1000)))
main()