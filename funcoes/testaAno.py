

import Ano

visitaPrimavera = 0
maior = 0
contvisitas = 0
for i in range (6):
    m = str.title(input("Digite um mês: "))
    visita = int(input("Digite a quantidade de visitantes: "))
    contvisitas += visita
    if (Ano.defineEstacao(m) == "Primavera"):
        visitaPrimavera += visita
    if (visita > maior):
        maior = visita
        maiorMes = m


print (f"Total de visitantes na primavera: {visitaPrimavera}") 
print (f"Mês com mais visitantes: {Ano.defineEstacao(maiorMes)}")
print (f"Total de Visitantes: {contvisitas}")