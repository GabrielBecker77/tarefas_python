"""Escreva um programa em Python que:
a) Leia uma lista com as temperaturas médias registradas durante 7 dias consecutivos.
b) Implemente uma função chamada media(temperaturas) que calcule e retorne a temperatura média da semana.
c) Implemente uma função chamada acima_da_media(temperaturas) que retorne uma nova lista contendo apenas as temperaturas acima da média.
d) Exiba no programa principal um menu com as seguintes opções:
Menu
1 - Exibe todas as temperaturas da semana
2 - Exibe a temperatura média da semana
3 - Exibe a lista de temperaturas acima da média
4 - Exibe a maior e a menor temperaturas da semana
5 - Sair"""
def maior(temperaturas):
    maiortemp = max(temperaturas)
    return maiortemp

def menor(temperaturas):
    menortemp = min(temperaturas)
    return menortemp

def media(temperaturas):
    temp_media = sum(temperaturas) / len(temperaturas)
    return temp_media

def acima_media(temperaturas):
    m = media(temperaturas)
    return [t for t in temperaturas if t > m]

temperaturas = [0] * 7

print("Digite as temperaturas dos últimos 7 dias da semana:")
for dia in range(7):
    temp = float(input(f"Dia {dia + 1}: "))
    temperaturas[dia] = temp

opcao = "0"
while opcao != 5:

    print("\n     Menu \n 1 - Exibe todas as temperaturas da semana \n 2 - Exibe a temperatura média da semana \n 3 - Exibe a lista de temperaturas acima da média \n 4 - Exibe a maior e a menor temperaturas da semana \n 5 - Sair")
    opcao = int(input())
    if opcao == 1:
        for i in range(7):
            temp_str = f"{temperaturas[i]:.2f}".rstrip('0').rstrip('.')
            print(f"Dia {i + 1}: {temp_str}°C", end='  ')
        print()

    elif opcao == 2:
        print(f"Temperatura média da última semana: {media(temperaturas):.0f}°C",end='  ')

    elif opcao == 3:
        m = media(temperaturas)
        temp_altas = acima_media(temperaturas)
        print("Dias em que a temperatura ultrapassou a média:")
        for i, temp in enumerate(temperaturas):
            if temp > m:
                print(f"Dia {i + 1}: {temp:.0f}°C", end='  ')
    elif opcao == 4:
        print(f"A maior temperatura registrada na última semana foi de {maior(temperaturas):.0f}°C e a menor foi {menor(temperaturas):.0f} °C.")

    else:
        print("Tchau")
        break