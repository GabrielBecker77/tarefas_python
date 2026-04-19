#Uma empresa decidiu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
salario = int(input())
if salario <0:
    print ("salario invalido")
else:
    if salario <=1000:
        aumento = 0.25
    elif salario <=2000:
        aumento = 0.20
    elif salario <=3000:
        aumento = 0.15
    else:
        aumento = 0.10
    valor_aumento = salario * aumento
    novosalario = salario + valor_aumento
    aumentovisivel = aumento * 100

    print (f"O percentual de aumento será de {aumentovisivel:.0f}%")
    print (f"O valor do aumento será de: R${valor_aumento:.2f}")
    print (f"E o novo salário será de: R${novosalario:.2f}")