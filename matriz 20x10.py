from random import seed
from random import randint

matriz = []
matrizmulti = []


for x in range(20):
    linha = []
    for y in range(10):
        linha.append(randint(0,10))
    matriz.append(linha)

print("Matriz original:")
for x in range(20):
    for y in range(10):
        print("%3d" % matriz[x][y], end=" ")
    print()

print()

somatoria = []

soma = 0

for x in range(21):
    somatoria.append(soma)
    for y in range(10):
        if x == 20:
            soma = soma + matriz[19][y]
        else:
            soma = soma + matriz[x][y]

somatoria.remove(0)

print("Vetor com a somatória de cada linha:")
print(somatoria)

print()

for x in range(20):
    linhamulti = []
    for y in range(10):
        multi = matriz[x][y]*somatoria[x]
        linhamulti.append(multi)
    matrizmulti.append(linhamulti)
    
print("matriz depois da multiplicação:")
for x in range(20):
    for y in range(10):
        print("%4d" % matrizmulti[x][y], end=" ")
    print()