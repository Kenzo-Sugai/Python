from placas import letras, numeros, placa

def main():
    numero = numeros()
    letra = letras()
    montarplaca = placa(letra, numero)
    print("Placa =", end=" ")
    for i in montarplaca:
        print(i, end="")

if __name__ == "__main__":
    main()