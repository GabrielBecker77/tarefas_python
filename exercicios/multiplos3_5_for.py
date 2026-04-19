"""#Escrever um programa que mostre os números múltiplos de 3, os múltiplos de 5 e os múltiplos de ambos, existentes entre 301 e 401.
for n in range(301,402):
    if n % 5 == 0 and n % 3 ==0:
        print(n, "- multiplo de 3 e de 5.")
    elif n % 3 ==0:
        print(n,"- multiplo de 3.")
    elif n % 5 == 0:
        print (n,"- multiplo de 5.")
"""

"""#Escrever um programa que mostre os números múltiplos de 3 e de 5 existentes entre 301 e 401.
# Os números múltiplos de 3 devem ser mostrados em azul e os múltiplos de 5 em amarelo.
# Quando o número for múltiplo de 3 e de 5, ele deverá ser mostrado em rosa (purple).
# Se não for múltiplo nem de 3 e nem de 5, deverá ser mostrada em branco.

BLUE   = "\033[1;34m"  # Azul
YELLOW = "\033[1;33m"  # Amarelo
PURPLE = "\033[1;35m"  # Roxo (Rosa)
WHITE  = "\033[1;37m"  # Branco
RESET  = "\033[0m"     # Resetar cor

for n in range(301,402):
        if n % 15 == 0:
                print(PURPLE + str(n), "- multiplo de 3 e de 5." + RESET)
        elif n % 3 == 0:
                print(BLUE + str(n), "- multiplo de 3." + RESET)
        elif n % 5 == 0:
                print(YELLOW + str(n), "- multiplo de 5." + RESET)
        else:
                print(WHITE +str(n), "- não é multiplo." + RESET) """

"""# Definições de cores
BLUE   = "\033[1;34m"  # Azul
YELLOW = "\033[1;33m"  # Amarelo
PURPLE = "\033[1;35m"  # Roxo (Rosa)
WHITE  = "\033[1;37m"  # Branco
RESET  = "\033[0m"     # Resetar cor

# Linha para ir preenchendo
linha = ""

for n in range(301, 402):
    if n % 15 == 0:
        cor = PURPLE
    elif n % 3 == 0:
        cor = BLUE
    elif n % 5 == 0:
        cor = YELLOW
    else:
        cor = WHITE

    linha += f"{cor}{n:>4}{RESET}"

    # A cada 10 números, quebra a linha
    if (n - 300) % 10 == 0:
        print(linha)
        linha = ""

# Imprime o que sobrou (se sobrar)
if linha:
    print(linha)"""