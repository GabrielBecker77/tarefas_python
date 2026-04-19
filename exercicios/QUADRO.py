#Construir um programa que sorteie 100 valores randômicos para uma lista e em seguida exibe um menu com as seguintes opções que serão chamadas pelas
# com as seguintes funções:
#Menu
#1 – Mostra a média das notas
#2 – Mostra as notas que estão acima da média
#3 – Mostra as notas que estão acima da média
#4 – Sair

#Descrição das funções:

#Uma função que recebe uma lista de notas e calcula a média de todas as notas
#Uma função que recebe uma lista de notas e exibe as notas que estão acima da média (essa função chama a função anterior para calcular a média)
#Uma função que recebe uma lista de notas e exibe as notas que estão abaixo da média (essa função chama a função anterior para calcular a média)

import random
lista = []
for _ in range(100):
    num = random.randint(0,100)
    lista.append(num)
print(lista)