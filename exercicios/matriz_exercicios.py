#1.  Construir um programa que gere valores aleatórios para uma matriz 5x5 e em seguida apresente e execute o seguinte menu
# (utilize o laço while para mostrar as opções e pedir que o usuário escolha uma alternativa):
#Mostrar a matriz formatada
#Mostrar a primeira linha
#Mostrar a primeira coluna
#Mostrar uma determinada posição solicitada pelo usuário (e validada pelo programa).
#Sair

import numpy as np
matriz = np.random.randint(0, 1000,(5,5))
opc = 0

while opc != 5:
    print("MENU")
    print("1 - Mostrar a matriz formatada.")
    print("2 - Mostrar a primeira linha.")
    print("3 - Mostrar a primeira coluna.")
    print("4 - Determinar posição a ser mostrada.")
    print("5 - Sair.")
    try:
        opc = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if opc == 1:
        print(matriz)

    elif opc == 2:
        print(matriz[0])

    elif opc == 3:
        print(matriz[:,0])

    elif opc == 4:
        try:
            linha = int(input("Digite o número da linha (0 a 4): "))
            coluna = int(input("Digite o número da coluna (0 a 4): "))
            if 0 <= linha <= 4 and 0 <= coluna <= 4:
                print(f"\nValor na posição [{linha}, {coluna}] é: {matriz[linha, coluna]}")
            else:
                print("Linha ou coluna fora do intervalo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")

    elif opc == 5:
        print("Saindo do programa...")

    else:
        print("Opção inválida. Tente novamente.")




#2.  Construir um programa que gere valores aleatórios (entre 0 e 100) para uma matriz 5x5 e em seguida apresente/execute o
# seguinte menu (utilize o laço while para mostrar as opções e pedir que o usuário escolha uma alternativa):

#Mostrar a matriz
#Mostrar o maior e o menor valores da matriz
#Mostrar a média de todos os valores da matriz
#Sair

import numpy as np

matriz = np.random.randint(0, 100, (5,5))
opc = 0

while opc != 4:
    print("Menu")
    print("1 - Mostrar Matriz")
    print("2 - Mostrar o maior e o menor valor da matriz")
    print("3 - Mostrar a média de todos os valores da matriz")
    print("4 - Sair")
    try:
        opc = int(input("Escolha uma opção:"))
    except ValueError:
        print("Digite um número válido:")
        continue
    if opc == 1:
        print(matriz)
    elif opc == 2:
        maior = np.max(matriz)
        menor = np.min(matriz)
        print(f"O maior valor na matriz é {maior} e o menor é {menor}")
    elif opc == 3:
        media = np.mean(matriz)
        print(media)

    elif opc == 4:
        break

    else:
        print("Opção inválida. Tente novamente.")








