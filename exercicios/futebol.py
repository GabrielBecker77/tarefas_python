#Construir um algoritmo para verificar qual dos dois times foi o vencedor dos jogos do último final de semana.
#Devem ser solicitados os nomes dos dois times e o número de gols realizados por cada um deles.
# Ao final deve ser apresentado o resultado do jogo, com o vencedor, ou informando caso tenha havido um empate.
time1 = input("Olá! Por favor informe o nome do time:")
golstime1 = int(input("A quantidade de gols:"))
time2 = input("Qual é o outro time:")
golstime2 = int(input("Quantos gols fizeram:"))

if golstime1 > golstime2:
    print("O", time1,"foi vencedor com o resultado de",golstime1,"a",golstime2,".")
elif golstime1 == golstime2:
    print ("empate")
else:
    print("O", time2, "foi vencedor com o resultado de", golstime2, "a", golstime1,".")