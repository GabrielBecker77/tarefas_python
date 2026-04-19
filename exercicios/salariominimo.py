#Para vários tributos, a base de cálculo é o salário mínimo. Elabore um algoritmo que leia o valor do salário mínimo e o valor do salário de uma pessoa.
#Calcular e mostrar quantos salários mínimos essa pessoa ganha.
print ("Olá! Por favor, informe o valor do salário mínimo e o valor do seu salário.")
sm = int(input())
s = int(input())
#1518
if s < sm:
    print ("EXPLORAÇÃO")
if s == sm:
    print ("Voce recebe um salário mínimo.")
if s > sm and s < (sm * 2):
    print ("Voce recebe pouco mais de um salário mínimo.")
if s > (sm * 2) and s < (sm * 3):
    print ("Voce recebe mais de dois salários mínimos.")

if s > (sm * 3) and s < (sm * 4):
    print ("Voce recebe mais de três salários mínimos.")
if s > (sm * 4):
    print ("burgues safado")