pontos_si = []
pontos_lcc = []
quant_empate = 0
vitorias_lcc = 0
vitorias_si = 0

quant_provas = int(input("Qual a quantidade de provas desse ano?"))

#Entrada de Dados
for i in range (1, quant_provas + 1):
    pontuacao_lcc = int(input(f"Qual a pontuação da {i}º prova de LCC? "))
    pontuacao_si = int(input(f"Qual a pontuação da {i}º prova de SI? "))
    pontos_lcc.append(pontuacao_lcc)
    pontos_si.append(pontuacao_si)

#Contagem de pontos
for i in range (quant_provas):
    if (pontos_lcc[i] > pontos_si[i]):
        vitorias_lcc += 1
    elif (pontos_si[i] > pontos_lcc[i]):
        vitorias_si += 1
    else:
        quant_empate += 1
    
#Definição do time campeão
timecampeao = "LCC" if vitorias_lcc > vitorias_si else "SI" if vitorias_lcc < vitorias_si else "EMPATE"

#Print dos resultados
print (f"Vitórias LCC: {vitorias_lcc}")
print (f"Vitórias SI: {vitorias_si}")
print (f"Empates: {quant_empate}")
print (f"Resultado: {timecampeao}")
