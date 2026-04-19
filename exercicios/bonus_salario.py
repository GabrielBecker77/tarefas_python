#Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
#Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

print ("Olá! Por favor, informe seu nome, seu salário fixo e o valor total de vendas que fez no mês.")
nome = input()
salario = float(input())
vendas = float(input())

bonus = vendas * 0.15
total = salario + bonus

print (nome,f"com sua bonificação o salário desse mês ficará em R$ {total:.2f}")