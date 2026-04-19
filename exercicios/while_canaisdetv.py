""" (1 com WHILE)
Construir um programa para registrar os dados referentes a preferência por canais de TV de pessoas entrevistadas.
O usuário deve informar os seguintes dados de cada cliente entrevistado:
Canal de TV que assiste mais (sendo 1-Globo, 2-SporTV, 3-Outra)
Canal de streaming que assiste mais (sendo 1-Netflix, 2-Disney, 3-Outra)
Idade da pessoa
Nível de instrução (1 – ensino fundamental, 2- ensino médio, 3- ensino superior)

Quando terminar de entrevistar as pessoas (respondendo à pergunta “Deseja continuar (S/N)?” ), deve ser apresentadas as seguintes informações:

Canais de TV aberto e streaming mais assistidos
Idade média das pessoas que assistem SporTV
Nível de instrução das pessoas que responderam à pesquisa (percentual de cada)
"""
# contadores
globo = 0
sportv = 0
outratv = 0
netflix = 0
disney = 0
outrostm = 0
idadetotal = 0
fund = 0
medio = 0
superior = 0
entrevistas = 0
resp = "S"

while resp == 'S':
    ctv = int(input("Qual canal de TV você assiste mais?\n1-Globo 2-SporTV 3-Outra:\n"))
    while ctv != 1 and ctv != 2 and ctv != 3:
        ctv = int(input("Opção inválida. Informe 1, 2 ou 3: "))

    if ctv == 1:
        globo += 1
    elif ctv == 2:
        sportv += 1
    else:
        outratv += 1

    cst = int(input("Qual canal de streaming você mais assiste?\n1-Netflix 2-Disney 3-Outra:\n"))
    while cst != 1 and cst != 2 and cst != 3:
        cst = int(input("Opção inválida. Informe 1, 2 ou 3: "))

    if cst == 1:
        netflix += 1
    elif cst == 2:
        disney += 1
    else:
        outrostm += 1
    idade = int(input("Qual sua idade?\n"))
    idadetotal += idade

    ensino = input("Qual seu nível de instrução?\n1-Fundamental 2-Médio 3-Superior:\n").strip()
    while ensino not in ("1", "2", "3"):
        ensino = input("Opção inválida. Informe 1, 2 ou 3: ").strip()

    if ensino == "1":
        fund += 1
    elif ensino == "2":
        medio += 1
    else:
        superior += 1

    entrevistas += 1
    resp = input("Deseja continuar? (S/N)").strip().upper()

# canal de TV mais assistido
if globo >= sportv and globo >= outratv:
    tv1 = "Globo"
elif sportv >= globo and sportv >= outratv:
    tv1 = "SporTV"
else:
    tv1 = "Outra"

# canal de streaming mais assistido
if netflix >= disney and netflix >= outrostm:
    stm1 = "Netflix"
elif disney >= netflix and disney >= outrostm:
    stm1 = "Disney"
else:
    stm1 = "Outra"

# idade média SporTV
if sportv > 0:
    idademedia = idadetotal / sportv
else:
    idademedia = 0

# percentuais por nível de instrução
perc_fundamental = (fund / entrevistas) * 100
perc_medio = (medio / entrevistas) * 100
perc_superior = (superior / entrevistas) * 100

# saída final
print("\n--- Resultados da Pesquisa ---")
print(f"Canal de TV mais assistido: {tv1}")
print(f"Canal de Streaming mais assistido: {stm1}")
print(f"Idade média dos que assistem SporTV: {idademedia:.0f} anos")
print("\nDistribuição do nível de instrução:")
print(f"Ensino Fundamental: {perc_fundamental:.2f}%")
print(f"Ensino Médio: {perc_medio:.2f}%")
print(f"Ensino Superior: {perc_superior:.2f}%")
