dicionario1 = {}
dicionario2 = {}

def anagrama(palavra1, palavra2):
    for letra in palavra1:
        if letra not in dicionario1:
            dicionario1[letra] = 1
        else:
            dicionario1[letra] += 1
    for letra in palavra2:
        if letra not in dicionario2:
            dicionario2[letra] = 1
        else:
            dicionario2[letra] += 1
   
def main():
    palavra1 = input("Insira a primeira palavra: ")
    palavra2 = input("Insira a segunda palavra: ")
    anagrama(palavra1, palavra2)
    if dicionario1 == dicionario2:
        print("%s e %s são anagramas!"% (palavra1, palavra2))
    else:
        print("%s e %s não são anagramas"% (palavra1, palavra2))
main()