from operator import itemgetter

texto = open("computacao.txt", 'r', encoding="utf8")
texto = texto.readlines()
txt1 = "".join(texto)
txt2 = "".join(texto)

txt1 = txt1.replace("!", "")
txt1 = txt1.replace("?", "")
txt1 = txt1.replace(",", "")
txt1 = txt1.replace(".", "")                                    
txt1 = txt1.replace(" ", "")

txt2 = txt2.replace("!", "")
txt2 = txt2.replace("?", "")
txt2 = txt2.replace(",", "")
txt2 = txt2.replace(".", "")
contagem = 0
for letras in txt1:
    contagem += 1
maior = 0
listapalavras = txt2.split()
dicionario = {}
for palavras in range(len(listapalavras)):
    dicionario[listapalavras[palavras]] = len(listapalavras[palavras])

dicionario = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print("Total de letras: %d"% contagem)
print("Mais longas:")
for x in range(0, 5):
    print(dicionario[x],"letras")