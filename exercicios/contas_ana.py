juros = 0.03
print (" Olá Ana Maria, vou ajuda-la com sua contabilidade. \n Me diga por favor, quanto voce recebe de salario?")
salario = int(input())
print ("Ok! E quanto é o valor total das suas contas?")
contas = int(input())

valordejuros = juros * contas
totalcontas = (int(valordejuros + contas))
restante = salario - totalcontas

print (f"Ana, o valor total de suas despesas será de R${totalcontas:.2f}, e o que sobra pra voce guardar é o valor de R${restante:.2f}.")