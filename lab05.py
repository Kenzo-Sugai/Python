salario = float(input("Digite o valor do seu atual salario: "))

# Calculo para o aumento:

if salario >= 0 and salario <= 400:
    aumento = salario*1.15
    print("Seu aumento será: R$ %.2f"% aumento)
elif salario >= 400.01 and salario <= 800.00:
    aumento = salario*1.12
    print("Seu aumento será: R$ %.2f"% aumento)
elif salario >= 800.01 and salario <= 1200.00:
    aumento = salario*1.10
    print("Seu aumento será: R$ %.2f"% aumento)
elif salario >= 1200.01 and salario <= 2000.00:
    aumento = salario*1.07
    print("Seu aumento será: R$ %.2f"% aumento)
elif salario > 2000.00:
    aumento = salario*1.04
    print("Seu aumento será: R$ %.2f"% aumento)
else:
    print("Valor inválido!"