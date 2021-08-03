def encontrarpalavras(palavra):
    arquivo = open("chat.txt", "r")
    for line in arquivo:
        line.strip().split('\n')
        if palavra in line:
            print(line)
    arquivo.close()
encontrarpalavras("Yes")