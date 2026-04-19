
notas = [0]*5

print("Informe as notas de 5 alunos:")
for i in range(5):
    notas[i] = float(input())

for i in range(5):
    print(f"O aluno {i+1} teve a nota {notas[i]:.2f}.")

soma = 0
for i in range(5):
    soma += notas[i]

media = soma/5
print(f"A média da turma foi {media:.2f}.")







n = int(input("Informe um numero:"))
t = [0]*11

for i in range(11):
    t[i] = i * n;

for i in range(11):
    print(f"{i:2} X {n:2} = {t[i]:3}")
