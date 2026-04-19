#Elabore um algoritmo para ler três valores e verificar se eles podem ser os comprimentos dos lados de um triângulo, e se forem, dizer o tipo de triângulo.
#Para ser um triângulo é necessário que qualquer um dos lados seja menor que a soma dos outros dois lados. (A < B+C) (B < A+C) (C < A+B).
#Para verificar qual o tipo de triângulo, seguimos as seguintes regras:
#Equilátero é aquele que tem os três lados iguais. (A = B = C)
#Isósceles é aquele que tem dois lados iguais. (A = B ) ou  (A = C) ou  (B = C)
#Escaleno é aquele que tem todos os lados diferentes (A  ≠ B ≠ C)
a = float(input("Digite o comprimento do primeiro lado: "))
b = float(input("Digite o comprimento do segundo lado: "))
c = float(input("Digite o comprimento do terceiro lado: "))
# Verifica se os valores formam um triângulo
if a < b + c and b < a + c and c < a + b:
    # Verifica o tipo de triângulo
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores informados não formam um triângulo.")
