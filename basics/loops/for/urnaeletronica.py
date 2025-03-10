
qtddevotosdocandidato1 = 0
candidato1 = "MARCÍLIO"
candidato2 = "AURÉLIO"
qtddevotosdocandidato2 = 0
qtddebranco = 0
for voto in range (4):
    votacao = str.upper(input("Qual o candidato escolhido? "))
    if (votacao == candidato1):
        qtddevotosdocandidato1 += 1
    elif (votacao == candidato2):
        qtddevotosdocandidato2 += 1
if (qtddevotosdocandidato2 > qtddevotosdocandidato1):
    ganhador = candidato2
elif (qtddevotosdocandidato2 < qtddevotosdocandidato1):
    ganhador = candidato1
else:
    ganhador = "NOVA VOTAÇÃO"
print (ganhador)

