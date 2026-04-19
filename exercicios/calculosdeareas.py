#Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.
valora, valorb, valorc = map(float, input().split())
pi = 3.14159
c2 = valorc * valorc

areatriangulo = (valora * valorc) / 2
areacirculo = pi * c2
areatrapezio = (valora + valorb) * valorc / 2
areaquadrado = valorb * valorb
arearetangulo = valora * valorb

print(f"TRIANGULO: {areatriangulo:.3f}")
print(f"CIRCULO: {areacirculo:.3f}")
print(f"TRAPEZIO: {areatrapezio:.3f}")
print(f"QUADRADO: {areaquadrado:.3f}")
print(f"RETANGULO: {arearetangulo:.3f}")