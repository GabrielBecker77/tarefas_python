##Implemente um algoritmo que leia as notas de 10 alunos armazenando-as em um vetor (matriz) de 10 posições.
#Ao final, escreva na tela somente as notas maiores que 5.0.


notas = []

print("Digite as notas de 10 alunos:")

# Leitura das notas
for i in range(10):
    nota = float(input(f"Nota do aluno {i+1}: "))
    notas.append(nota)

print("\nNotas maiores que 5.0:")

# Exibição das notas maiores que 5.0
for nota in notas:
    if nota > 5.0:
        print(nota)



#Desenvolva um algoritmo que leia um conjunto de 15 números inteiros e armazene-os em um vetor A.
#Após a leitura dos dados o algoritmo deve multiplicar todos os números do vetor A por 3 e armazenar o resultado em um segundo vetor B. No final, mostrar o conteúdo dos 2 vetores.

a = [0]*15
b = [0]*15
for i in range(15):
    a[i] = int(input("Informe um número inteiro:"))
for i in range(15):
    b[i] = a[i] * 3

print("\nÍndice |  A  |  B (A*3)")
print("------------------------")
for i in range(15):
    print(f"{i:>6} | {a[i]:>3} | {b[i]:>6}")



A = []
B = []
print ("Informe 15 números inteiros.")
for i in range(15):
    numero = int(input(f"Informe o {i+1}º número: "))
    A.append(numero)

for i in range (15):
    B.append(A[i] * 3)

print("Vetor A original:")
print(A)

print("Vetor B após a multiplicação:")
print(B)


#Elabore um algoritmo que leia valores inteiros para um vetor com 10 números e calcule a diferença entre o maior e o menor elemento existente.
numeros = []
print("Informe 10 números inteiros:")
for i in range(10):
    num = int(input(f"Informe o {i+1} número: "))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)
diferenca = maior - menor

# Exibe o resultado
print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")
print(f"Diferença entre o maior e o menor: {diferenca}")




#Elabore um algoritmo que leia valores inteiros para um vetor com 10 números e calcule a diferença entre as posições que maior e o menor elemento existentes ocupam.

# Inicializa o vetor
numeros = []

print("Digite 10 números inteiros:")

# Leitura dos 10 números
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Encontra as posições (índices) do maior e menor elemento
pos_maior = numeros.index(max(numeros))
pos_menor = numeros.index(min(numeros))

# Calcula a diferença entre as posições
diferenca_posicoes = abs(pos_maior - pos_menor)

# Exibe os resultados
print(f"\nVetor lido: {numeros}")
print(f"Maior número: {numeros[pos_maior]} na posição {pos_maior}")
print(f"Menor número: {numeros[pos_menor]} na posição {pos_menor}")
print(f"Diferença entre as posições: {diferenca_posicoes}")








#Implemente um algoritmo que leia as notas e os nomes de 5 alunos armazenando os dados em vetores de 5 posições,
# sendo que as notas serão armazenadas em um vetor de números reais e os nomes em um outro vetor do tipo string.
# Ao final o algoritmo deve escrever na tela somente os nomes dos alunos que tiraram nota maior que 5.0.

notas = [0] * 5
nomes = [0] * 5

for i in range(5):
    nomes[i] = input("Qual seu nome? ")
    notas[i] = float(input("Qual foi a sua nota? "))
[print(nome) for nome, nota in zip(nomes, notas) if nota > 5]





#Algoritmo que leia o nome e a altura de 5 pessoas, armazenando os dados em dois vetores e que mostre o nome da pessoa mais alta e
# o nome da pessoa mais baixa com suas respectivas alturas. Note que não poderá ordenar o vetor de alturas, do contrário perderá a “ligação” com o vetor de nomes.

nomes = [0] * 5
alturas = [0] * 5

for i in range(5):
    print("Por favor informe seu nome e sua altura.")
    nomes[i] = input()
    alturas[i] = float(input())

pos_alto = 0
pos_baixo = 0

for i in range(1,5):
    if alturas[i] > alturas[pos_alto]:
        pos_alto = i
    if alturas[i] < alturas[pos_baixo]:
        pos_baixo = i

print(f"A pessoa mais alta é {nomes[pos_alto]} com {alturas[pos_alto]:.2f} m")
print(f"A pessoa mais baixa é {nomes[pos_baixo]} com {alturas[pos_baixo]:.2f} m")





"""
"""

listaInteiros = [10, 20, 40, 50]
listaInteiros.append(60)  # insere o valor 60 no final da lista
listaInteiros.insert(2, 30)  #insere o valor 30 na posição 2 (terceira posição)
for i in range(len(lista)):

