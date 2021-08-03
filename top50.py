import os
from time import sleep


red   = "\033[1;31m"  
blue  = "\033[1;34m"
cyan  = "\033[1;36m"
green = "\033[0;32m"
reset = "\033[0;0m"
bold    = "\033[;1m"
reverse = "\033[;7m"





def adicionaranime():
    nome = input("Adicione o nome do anime: ")
    if os.path.isfile("./animes/%s.txt"% nome):
        print(red+"Anime já registrado"+reset)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        arquivo = open("./animes/%s.txt"% nome, "w")
        arquivo.write("0")
        arquivo.close()
        print(green+"Anime adicionado com sucesso!"+reset)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

def removeranime():
    nome = input("Digite o nome do anime que queira remover: ")
    if os.path.isfile("./animes/%s.txt"%nome):
        os.remove("./animes/%s.txt" %nome)
        print(green+"Anime excluido com sucesso!"+reset)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(red+"Esse Anime não existe!"+reset)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

def estatisticas():
    while True:
        print(bold+"""
        ||*---------------- estatísticas ----------------*||

        (1) - Assistidos

        (2) - Top

        (3) - Estatísticas

        (4) - Voltar ao menu

        """+reset)

        n = input("Escolha um número: ")

        if n == "1":
            os.listdir("./animes/")
            
        elif n == "2":
            pass
        elif n == "3":
            pass
        elif n == "4":
            return main()


def main():
    while True:
        print(bold+"""
        ||*---------------- menu ----------------*||

        (1) - Adicionar anime

        (2) - Remover anime

        (3) - Estatísticas

        (4) - Sair

        """+reset)
        
        n = input("Escolha um número: ")
        
        if n == "1":
            adicionaranime()
        elif n == "2":
            removeranime()
        elif n == "3":
            estatisticas()
        elif n == "4":
            break
main()