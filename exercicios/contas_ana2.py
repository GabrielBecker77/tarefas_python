#Ana Maria recebeu seu salário e precisa pagar 2 contas que já venceram. Como as contas estão atrasadas,
# Ana Maria terá que pagar multa de 3% sobre cada conta.  Precisamos ajudar!
#Vamos construir um programa que solicite o salário de Ana Maria e o valor de suas contas.
#O programa deve calcular e mostrar o total suas despesas e o quanto restará do salário de Ana Maria após pagar as contas.
#Lembre-se que não temos funções prontas para calcular percentual, assim, utilizamos “regra de três” e realizamos multiplicações
# e divisões para obter o resultado desejado.
#Vamos ajudar a Ana Maria?

print (" Olá Ana Maria, vou ajuda-la com sua contabilidade. \n Me diga por favor, quanto voce recebe de salario?")
salario = int(input())
print ("Ok! E quanto é o valor total das suas contas?")
contas = int(input())
print  ("E qual será o percentual de juros a pagar pelo atraso?")
juros = int(input())


jurosdecimal = juros / 100
valordejuros = jurosdecimal * contas
totalcontas = (int(valordejuros + contas))
restante = salario - totalcontas

print (f"Ana, o valor total de suas despesas será de R${totalcontas:.2f}, e o que sobra pra voce guardar é o valor de R${restante:.2f}.")


# outra opção de formatação
# ("Ana, o valor total de suas despesas será de R${}, e o que sobra pra voce guardar é o valor de R${}." .format(totalcontas, restante))
