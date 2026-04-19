"""
import random

numeros = [
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100)
]


pares = [0]*10
impares = [0]*10
qtd_pares = 0
qtd_impares = 0

i = 0
while i < 10:
    if numeros[i] % 2 == 0:
        pares[qtd_pares] = numeros[i]
        qtd_pares += 1
    else:
        impares[qtd_impares] = numeros[i]
        qtd_impares += 1
    i += 1

ordenados = [0]*10
i = 0
while i < 10:
    ordenados[i] = numeros[i]
    i += 1

i = 0
while i < 9:
    j = 0
    while j < 9 - i:
        if ordenados[j] > ordenados[j + 1]:
            temp = ordenados[j]
            ordenados[j] = ordenados[j + 1]
            ordenados[j + 1] = temp
        j += 1
    i += 1

soma = 0
i = 0
while i < 10:
    soma += numeros[i]
    i += 1
media = soma / 10



print("Números sorteados:")
print(numeros)
print("Números pares:")
i = 0
while i < qtd_pares:
    print(pares[i])
    i += 1
print("Números ímpares:")
i = 0
while i < qtd_impares:
    print(impares[i])
    i += 1
print("Números ordenados:")
print(ordenados)
print("Média dos números:", media)




#Construir um programa que gere números aleatórios ou randômicos entre 0 e 100, até que o valor zero seja sorteado. Em seguida mostre os dois maiores valores sorteados.
import random
numeros = []

while True:
    n = random.randint(0, 100)
    print(f"Sorteado: {n}")
    if n == 0:
        break
    numeros.append(n)

if len(numeros) < 2:
    print("Houve menos que dois números.")
else:
    total = len(numeros)
    maior1 = max(numeros)
    numeros.remove(maior1)
    maior2 = max(numeros)

print (f"Foram sorteados {total} números, os maiores números sorteados foram:", maior1, maior2)




Construir um programa que solicite o nome, a idade e quantidade de filhos de uma quantidade indeterminada de pessoas enquanto o usuário responder
‘Sim’ (‘S’) a pergunta “Deseja continuar (S/N)?”.  Ao final apresente um relatório contendo:
O nome e idade da pessoa mais velha
O nome e quantidade de filhos da pessoa mais velha
O nome da pessoa com maior quantidade de filhos
maisvelho = 0
nomemaisvelho = "x"
nomemaisfilhos = "x"
filhosmaisvelho = 0
qtdfilhos = 0
opc = "S"
while opc != "N":
    nome = input("Qual o seu nome? ")
    idade = int(input("Qual a sua idade?"))
    filhos = int(input("Quantos filhos voce tem?"))
    opc = input("Deseja continuar? (S/N)").upper()

    if idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = (nome)
        filhosmaisvelho = filhos

    if filhos > qtdfilhos:
        nomemaisfilhos = nome
        qtdfilhos = filhos

print(f"A pessoa mais velha é {nomemaisvelho} com {maisvelho} anos, {nomemaisvelho} tem {filhosmaisvelho} filho. "
      f"A pessoa com mais filhos é {nomemaisfilhos}")













