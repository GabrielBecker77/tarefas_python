#Elabore um algoritmo que leia dois números inteiros e imprima a seguinte saída:
#Dividendo: Divisor: Quociente:  Resto:
#Para a resolução desse algoritmo utilize / , // e %.

print ("Por favor, informe dois números inteiros.")
n1 =  int(input())
n2 = int(input())


if n1>n2:
    dividendo = n1
    divisor = n2
    quociente = n1 // n2
    resto =  n1 % n2
else:
    dividendo = n2
    divisor = n1
    quociente = n2 // n1
    resto = n2 % n1

print ("O dividendo será", dividendo,", o divisor será", divisor,", o quociente será",quociente,",e o resto da divisão será de", resto,".")