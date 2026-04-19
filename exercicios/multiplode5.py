#Escrever um algoritmo que leia um número inteiro e verifica se é múltiplo de 5.  Informar ao usuário o resultado.
#Em seguida, se o número for múltiplo, mostrar o número dividido por 10 (formatado com 2 casas decimais), senão escrever o número multiplicado por 10.
print ("Olá! Por favor informe um número inteiro.")
N = int(input())

RED   = "\033[1;31m"
GREEN = "\033[0;32m"

if N % 5 == 0:
    print (GREEN + "É múltiplo de 5")
else:
    print (RED + "Não é múltiplo de 5.")