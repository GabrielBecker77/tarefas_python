#Atividade para entregar
#Escreva um programa que faça as seguintes perguntas ao usuário:
#a) Você fez exercício físico hoje? (S/N)
#b) Você alongou o corpo hoje? (S/N)
#Se a resposta às duas perguntas for "S", o programa deve exibir: "Muito bem! Seu corpo agradece!". Caso contrário, exiba: "Que tal se movimentar um pouco?".

resp1 = input("Olá! Tudo bem? Você já se alongou hoje? (S/N)")
resp2 = input("E práticou atividade física? (S/N)")

resp1 = resp1.upper()
resp2 = resp2.upper()

if resp1 == "S" and resp2 == "S":
    print ("Muito bem! Seu corpo agradece!")


elif resp1 == "N" and resp2 == "S":
    print ("É sempre bom se alongar antes de qualquer atividade física, mas mesmo assim muito bom!")


else:
    print ("Que tal se movimentar um pouco?")
