#Elabore um algoritmo que leia três números reais, num1, num2 e num3 e imprima o valor de y, sabendo-se que:

#y = num1 +     num2          + 2*(num1 – num2)
#                            num3 + num1
num1 = float(input("Por favor digite o primeiro número:"))
num2 = float(input("Por favor digite o segundo número:"))
num3 = float(input("Por favor digite o terceiro número:"))

numerador = num1 + num2 + 2 * (num1 - num2)
denominador = num3 + num1

if denominador != 0:
    y = numerador / denominador
    print(f"O valor de y é: {y}")
else:
    print("Erro: divisão por zero.")
