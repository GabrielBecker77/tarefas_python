#Dividendo: Divisor: Quociente:  Resto:
#Para a resolução desse algoritmo utilize / , // e %.

print ("Por favor informe um numero inteiro que será o Dividendo:")
n1 =  int(input())
print ("Por favor informe um numero inteiro que será o Divisor:")
n2 = int(input())

dividendo = n1
divisor = n2
quociente = n1 / n2
resto = n1 % n2
resultado_div_inteira = n1 // n2

if (n1 % n2) > 0:
    print("Essa é uma divisão exata, ou seja, o resto será 0.")
else:
    print("Essa é uma divisão NÃO exata, ou seja, o resto será 0.")

print ("- O Dividendo escolhido foi:", dividendo,
       ".\n- O Divisor escolhido foi:", divisor,
       ".\n- O Quociente desta divisão é:",quociente,
       ".\n- O Resultado inteiro da divisão é:", resultado_div_inteira,
       ".\n- O Resto da divisão é:",resto
       )
