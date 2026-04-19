#CORES
WHITE = "\033[1;29m"
BLACK = "\033[1;30m"
RED   = "\033[1;31m"
GREEN = "\033[0;32m"
YELLLOW = "\033[1;33m"
BLUE  = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN  = "\033[1;36m"
PURPLE = "\033[1;35m"  # Roxo (Rosa)
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
ITALIC = "\033[;3m"
UNDERSCORE = "\033[;4m"
REVERSE = "\033[;7m"


RED   = "\033[1;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

print(RED + "ERRO!" +  GREEN + "Alguma coisa deu errado..." + RESET)

"""
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

for n in range(301, 402):
    if n % 3 == 0 and n % 5 == 0:
        print(Fore.MAGENTA + str(n))  # Roxo/rosa
    elif n % 3 == 0:
        print(Fore.BLUE + str(n))
    elif n % 5 == 0:
        print(Fore.YELLOW + str(n))
    else:
        print(Fore.WHITE + str(n))
        """