#Durante uma pesquisa na turma de Algoritmos, foi solicitado que os 40 alunos informassem quantas horas costumam estudar por semana.
# Elabore um algoritmo em Python que leia essas 40 respostas (valores inteiros). Ao final, o programa deve informar:
#Quantos alunos estudam mais de 10 horas por semana.
#A média de horas de estudo apenas desses alunos.
mais_de_10 = []
for aluno in range(40):
    horas = int(input("Informe as horas de estudo: "))
    if horas > 10:
        mais_de_10.append(horas)

quantidade = len(mais_de_10)
media = sum(mais_de_10) / quantidade if quantidade > 0 else 0

print(quantidade,"alunos estudam mais de 10 horas por semana.")
print(f"Média de horas desses alunos: {media:.2f} horas")