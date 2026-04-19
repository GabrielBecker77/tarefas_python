quantidade = int(input("Quantos números você quer informar? "))

entrada = input(f"Digite os {quantidade} números separados por espaço: ")

numeros = list(map(float, entrada.split()))

if len(numeros) != quantidade:
    print("A quantidade de números digitados não corresponde ao valor informado!")
else:
    for numero in numeros:
        triplo = numero * 3
        print(f"O triplo de {numero} é {triplo}")