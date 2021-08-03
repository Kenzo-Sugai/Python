import math

a = int(input("Digite o valor de a: "))

if a == 0:
    print("Essa equação não é do segundo grau!")

else:
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    
    d = (b*b)-(4*a*c)
    
    if d < 0:
        print("Não existem raizes reais!")
    elif d >= 0:
        if d == 0:
            e = (-b)/(2*a)
            print("raiz: %.3f"% e)
        else:
            e1 = (-b+math.sqrt(d))/(2*a)
            e2 = (-b-math.sqrt(d))/(2*a)
            print("Primeira raiz: %.3f"% e1)
            print("Segunda raiz: %.3f"% e2)