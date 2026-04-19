#Segundo uma tabela médica, o peso ideal está relacionado com a altura e o sexo.
#Elabore um algoritmo que leia a altura e o sexo de uma pessoa (M/F), calcule e imprima seu peso ideal, utilizando as seguintes fórmulas.

#Para homens                   #Para mulheres
#(72,7 * altura) - 58          #(62,1 * altura) – 44,7
sexo=input("Por favor informe seu sexo (M/F):").strip().upper()
altura=float(input("Por favor informe sua altura:").replace(",", "."))
if altura <=0:
    print("Altura deve ser maior que 0.")
    peso = None
else:
    if sexo == "M":
        peso = (72.7 * altura) - 58
    elif sexo == "F":
        peso = (62.1 * altura) - 44.7
    else:
        print("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")
        peso = None

# Exibição do resultado
if peso is not None:
    print(f"Seu peso ideal é: {peso:.2f} kg")