#Elabore um algoritmo que imprima todos os números pares de 1 até 100.
contador = 0
for n in range(2,101,2):
    print(f"{n:4}", end ="")
    contador +=1
    if contador %10 ==0:
        print ()
#Otimização do código:
#Podemos eliminar a variável contador e usar enumerate para contar as iterações automaticamente:

#for i, n in enumerate(range(2, 101, 2), start=1):
#    print(f"{n:4}", end="")
#    if i % 10 == 0:
#        print()