"""Elabore um algoritmo que leia um número inteiro entre 1 e 6 e imprima o mês correspondente.
Caso seja digitado um valor entre 7 e 12, informar que é um mês localizado no segundo semestre do ano.
Caso seja digitado um valor fora desse intervalo, deverá ser exibida uma mensagem informando que não existe mês com esse número. """

mes = int(input("Por favor informe o número do mês:"))
match mes:
    case 1:
        print("Janeiro")
    case 2:
       print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7 | 8 | 9 | 10 | 11 | 12:
        print("Esse é um dos meses do segundo semestre do ano.")
    case _:
        print("Não existe mês com esse número.")