 # Escreva um programa que resolva uma equação de segundo grau.
 # -*- coding: utf-8 -*-

from math import sqrt
a = 3
b = 4
c = 1

y = 2

 # Equadação de segunda grau: b² - 4 a c

delta = b*b - 4*a*c

print("delta:",delta)

raiz_delta = sqrt(delta)

if delta<=0:
	print("Raiz inválida")
elif delta>=1:

	x1 = (-b + raiz_delta)/2*a
	x2 = (-b - raiz_delta)/2*a

print("as raizes da equação são",x1,x2)

