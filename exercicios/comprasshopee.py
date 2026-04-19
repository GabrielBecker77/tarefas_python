#Ana deseja fazer algumas comprinhas da Shopee e os produtos que ela deseja tem os seguintes valores:
# bule de louça – US$ 25,00, alimentador automático para gatos – US$13,00.  O frete para esses dois produtos é de R$14,00.
# Considerando que o valor da cotação do dólar é de R$5,70.  Qual será o valor total da compra de Ana em reais?
# Se ela precisar pagar IOF de 6% sobre os produtos comprados, de quanto s erá o valor do imposto em reais?



bule = 25
alimentador = 13
frete = 14
valordolar = 5.70
imposto = 6/100

valordosprodutosemdolar = bule + alimentador
valordosprodutosemreal = valordosprodutosemdolar * valordolar
valortotal = valordosprodutosemreal + frete
valordoimposto = valordosprodutosemreal * imposto

print (f"O valor total das compras em reais será de R${valortotal:.2f} e o valor do imposto pago em reais seria deR${valordoimposto:.2f}.")