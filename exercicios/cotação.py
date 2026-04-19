#Supondo que a cotação do dólar para câmbio seja de R$5,70 e a cotação do Peso Argentino seja de R$0,005.
# Quantos dólares e quantos pesos posso comprar com R$1214,00?
# Construa um programa com variáveis para calcular a quantidade de pesos e de dólares que posso comprar.

valordolar = 5.70
valorpeso = 0.005
QTDreais = 1214.0

QTDdolar = QTDreais / valordolar
QTDpeso = (float(QTDreais / valorpeso))

print (f"R${QTDpeso:.2f}.")
print (f"R${QTDdolar:.2f}.")