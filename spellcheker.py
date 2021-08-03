def spellChecker(words):
    check = words.split()
    arquivo = open("./words.txt", "r")
    palavras = arquivo.readlines()
    arquivo.close()
    print(check)
    checker = []
    for x in range(len(check)):
        for y in range(len(palavras)):
            if check[x] != palavras[y]:
               checker.append(check[x])
    print(checker)

spellChecker("2,4,5-t cASA")