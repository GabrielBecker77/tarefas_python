pesototal = 0
cont = 0

while cont < 7:
    peso = float(input("Informe o peso da próxima pessoa que vai entrar no elevador: "))

    if pesototal + peso > 500:
        print("Limite de peso excedido. Essa pessoa não pode entrar.")
        break  # para o loop se o peso for excedido

    pesototal += peso
    cont += 1

print("O número de pessoas que entrou foi:", cont)
print("O peso total foi:", pesototal)
