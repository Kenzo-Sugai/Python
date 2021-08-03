# Mensagem abaixo
# -*- coding: utf-8 -*-


# Testes

print("Olá Mundo")
print(2 % 3)
Xis = "Variável"
print(Xis)
print(Xis)
Xis2 = 1 # variável inteira
Xis3 = 1.1 # variável float
Xis4 = "String" # variável string
Xis5 = True # verdadeiro
Xis5 = False # vai se sobrepor ao "True"
print(Xis5)

x = 2
y = 1
z = 4 - 1
a = 0

print(x == y)

# Comandos matemáticos

x = y # Variável
x + y # Soma
x - y # Diferença
x * y # Produto
x % y # Razão
x += y # x = x + y
x ** y # Expoente
x == y # Igual
x != y # Diferente
x > y # Maior
x < y # Menor
x >= y # Maior ou Igual
x <= y # Menor ou Igual
x == y and x == z # Dois atributos verdadeiros
x == y or x == z # Um atributo verdadeiro

# Condições

if y < x:
	print("True") # Condição
elif x < y:
	print("This False") # Porém com condição
else:
	print("False!") # Porém

# Repetição

k = 5
while k < 10:
	print (k)
	k = k+1
Lista = [0,1,2,3,4,5]
for i in Lista:
	print(i)
for t in range(50,60):
	print(t)

# String

q = "TAMANHO"

p = q + q + "\n" # 7 + 7 = 14 / "\n (dar espaço, quebra de linha)"

m = "quebra de palavras ou linhas de acordo com o pedido"

TAMANHO = len(p) # Contar

print(TAMANHO)

busca = m.find("linhas") # diz o índice da localização da palavra

print(q[2]) # 0 = t / 1 = a / 2 = m (Tamanho) print(q[0:7]) # 0 = t até 7 = o (tamanho)
print(q.lower()) # Deixar maiúsculo em minúsculo 
print(q.upper()) # Deixar minúsculo em maiúsculo print(q.strip()) # Retirar os espaços/quebras de linhas
print(m.split(" ")) # Copia a frase/palavra quebrando-as de acordo
print(m[busca:]) # Copia o resto do texto a partir da localização pedida
print(m.replace("linhas", "colunas")) # Substituir palavras de um texto

# Funções

def soma(x, y): # Função de soma
	return x+y

def subtração(x, y): # Função de subtração
	return x-y

def multiplicação(x, y): # Função de multiplicação
	return x*y

sm = soma(6, 5) # Valores para a função de soma
sb = subtração(8, 2) # Valores para a função de subtração
mt = multiplicação(4, 3) # Valores para a função de multiplicação
al = soma(sb, mt) # Valores para a função de soma de duas funções

print(sm, sb, mt, al)

# Arquivos

arquivo = open("Arquivo.txt")

linhas = arquivo.readline() # Ler apenas linhas

print(linhas)

linhas1 = arquivo.read() # Ler texto completo

print(linhas1)

# Listas

lista1 = [1, 2, 3, 4] # Lista numérica
lista2 = ["casa", "amor", "arvore"] # Lista de palavras
lista3 = ["rua", 4, 3, 278, "muro", "computador", 12, 00] # Lista mista
lista4 = [23, 45, 1, 2, 100, 43, 124, 531, 90]
indice = len(lista1) # Conta lista
	
print(indice)

print(lista2)

if "cachorro" not in lista2: # Se não estiver na lista, printar:
	print("cachorro não está na lista")

lista2.append("cachorro") # Adicionar item na lista

print(lista2)

if "cachorro" in lista2: # Se estiver na lista, printar:
	print("cachorro está na lista")

del lista1[1:3] # Apagar entre o 1 e o 3
	
print(lista1)

lista4.sort() # Organizar lista de forma crescente

print(lista4)

lista4.sort(reverse=True) # Organizar a lista de forma decrescente (pode-se usar também [lista4.reverse()])

print(lista4)

# Dicionário

site = {"twitter":"twitter.com", "youtube":"youtube.com", "google":"google.com"} # Designar índice em uma lista como uma "chave"

print(site["twitter"]) # Apenas solicitando a impressão da "chave" 

for chave in site:
	print(chave +":"+ site[chave]) # Impressão da chave + índice

for itens in site.items(): # impressão dos intens (forma simplificada do comando anterior)
	print(itens)

for valores in site.values(): # Impressão apenas dos índices
	print(valores)

for chaves in site.keys(): # Impressão apenas das chaves
	print(chaves)

# Escolha de números aleatórios

import random

random.seed() # Setar um número fixo dos aleatórios (indicar o número nos parênteses)

aleatório = random.randint(0, 10) # Número aleatório

print(aleatório)

lista5 = [3,7,10]

escolher = random.choice(lista5)

print(escolher)

# Excessões

try:
	print(b/a)
except:
	print("Não é possível fazer divisão por 0")
