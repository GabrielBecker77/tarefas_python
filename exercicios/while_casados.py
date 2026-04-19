"""Elabore um algoritmo que leia a idade e o estado civil (C – casado, S – solteiro, V – viúvo, e D – divorciado ou T - convivente) de várias pessoas.
 Considere que o algoritmo termina quando se digita ‘N’ como resposta à pergunta “Deseja continuar (S/N)?’. Ao final, calcule e imprima:
a A quantidade de pessoas casadas;
b A idade da pessoa solteira mais velha
c A média das idades das pessoas viúvas;
d A porcentagem de pessoas conviventes, dentre todas as pessoas analisadas."""

casados = 0
solteiro_mais_velho = 0
soma_idade_viuvos = 0
qtd_viuvos = 0
qtd_conviventes = 0
total_pessoas = 0

# Loop para entrada de dados
continuar = 'S'
while continuar.upper() == 'S':
    idade = int(input("Digite a idade: "))
    estado_civil = input("Digite o estado civil (C - casado, S - solteiro, V - viúvo, D - divorciado, T - convivente): ").upper()

    total_pessoas += 1

    if estado_civil == 'C':
        casados += 1
    elif estado_civil == 'S':
        if idade > solteiro_mais_velho:
            solteiro_mais_velho = idade
    elif estado_civil == 'V':
        soma_idade_viuvos += idade
        qtd_viuvos += 1
    elif estado_civil == 'T':
        qtd_conviventes += 1

    continuar = input("Deseja continuar (S/N)? ")

# Cálculos finais
if qtd_viuvos > 0:
    media_viuvos = soma_idade_viuvos / qtd_viuvos
else:
    media_viuvos = 0

if total_pessoas > 0:
    porcentagem_conviventes = (qtd_conviventes / total_pessoas) * 100
else:
    porcentagem_conviventes = 0

# Saída de resultados
print("\nRESULTADOS:")
print(f"Quantidade de pessoas casadas: {casados}")
print(f"Idade da pessoa solteira mais velha: {solteiro_mais_velho}")
print(f"Média das idades das pessoas viúvas: {media_viuvos:.2f}")
print(f"Porcentagem de conviventes: {porcentagem_conviventes:.2f}%")