#Programa que conta a quantidade de alunos em uma escola a partir da consulta individual de turmas
total_alunos = 0
alunos_por_turma = []

for i in range (4):
    alunos = int(input("Quantos alunos tem na sua turma? "))
    alunos_por_turma.append(alunos)

for i in range (4):
    total_alunos += alunos_por_turma[i]

print (f"A quantidade total de alunos é: {total_alunos}")
