bule = 25
alimentador = 13
frete = 14
valordodolar = 5.70
imposto = 6/100
valordosprodutosemdolar = bule + alimentador
valordosprodutosemreais = valordosprodutosemdolar * valordodolar
valortotal = valordosprodutosemreais + frete
valordoimposto = valordosprodutosemreais * imposto

print ('O valor total das compras em reais será de {0:.2f}'.format (valortotal))
print ('Caso lhe seja cobrado o imposto de IOF, o imposto em reais será de {0:.2f}'.format(valordoimposto))