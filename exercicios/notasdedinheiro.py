#Leia um valor de ponto flutuante com duas casas decimais.
#Este valor representa um valor monetário.
#A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
#As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
# A seguir mostre a relação de notas necessárias.

# Lê o valor como ponto flutuante (ex: 576.73)
valor = float(input("Qual o valor:"))

# Converte para centavos e arredonda para evitar erros de precisão
centavos = int(round(valor * 100))

# Lista dos valores das notas em centavos
notas = [10000, 5000, 2000, 1000, 500, 200]

# Lista dos valores das moedas em centavos
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    qtd = centavos // nota                     # Calcula quantas notas cabem
    print(f"{qtd} nota(s) de R$ {nota / 100:.2f}")
    centavos %= nota                           # Atualiza o valor restante

print("MOEDAS:")
for moeda in moedas:
    qtd = centavos // moeda                    # Calcula quantas moedas cabem
    print(f"{qtd} moeda(s) de R$ {moeda / 100:.2f}")
    centavos %= moeda                          # Atualiza o valor restante