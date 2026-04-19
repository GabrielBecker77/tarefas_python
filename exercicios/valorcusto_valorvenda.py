
#Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%.
#Elabore um algoritmo que leia o valor do produto, calcule e imprima o valor de venda do produto.
custoproduto = float(input("Digite o custo do produto: R$ "))
if custoproduto <20:
    lucro = 0.45
else:
    lucro = 0.30
valordelucro = custoproduto * lucro
valordevenda = valordelucro + custoproduto


print(f"Valor de venda: R$ {valordevenda:.2f}")