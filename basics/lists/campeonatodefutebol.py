"""
# CÓDIGO ANTIGO ABAIXO

times_nome = []
times_estado = []
pontuacao = []
times_pe_pb = []
times_mg = []
pe_pb = []
soma_pontuacao_rj = 0
quant_times_rj = 0


qtdsdetimes = int(input("Qual a quantidade de times a ser inserida no sistema?"))

for count in range (qtdsdetimes):

    nome = (str.upper(input("Qual o nome do time?")))
    estado = (str.upper(input(f"Qual o estado do {nomedotime}")))
    pontos = (int(input("Qual a quantidade de pontos?")))
    
    times_nome.append(nome)
    times_estado.append(estado)
    pontuacao.append(pontos)
    
    
maior_pontuacao = pontuacao[0]

for i in range (qtdsdetimes):
    if (times_estado[i] == "PB") or (times_estado == "PE"):
        if (pontuacao[i] > 100):
            times_pe_pb.append(times_nome[i])
            times_pe_pb.append(times_estado[i])
            times_pe_pb.append(pontuacao[i])
            pe_pb += times_pe_pb
    elif (times_estado[i] == "MG"):
        times_mg.append(times_nome[i], times_estado[i], pontuacao[i])
    elif (times_estado[i] == "RJ"):
        soma_pontuacao_rj += pontuacao[i]
        quant_times_rj += 1
    if (maiorpontuacao < pontuacao[i]):
        maiorpontuacao = pontuacao[i]
        timemaiorpontuacao = times_nome[i]
    print (f"Time {(i+1)} {times_nome[i]}, {pontuacao[i]}pts")

if (soma_pontuacao_rj != 0):        
    mediadostimesdorj = soma_pontuacao_rj // quant_times_rj
    print (f"Média de pontos dos times do RJ: {mediadostimesdorj}")
else:
    print ("Nenhum time do RJ foi inserido")
if (len(times_pe_pb) != 0):
    print (f"Times de PB e PE com mais de 100 pontos: {pe_pb}")
else:
    print ("Nenhum time da PB ou de PE foi fornecido")
if (len(times_mg) != 0):
    print (f"Times de MG e suas pontuações: {times_mg}")
else:
    print ("Nenhum time de MG foi fornecido")    

"""

# CÓDIGO MELHORADO COM FUNÇÃO MAX, LAMBDA:

dicionario_estados = {

    "Minas gerais": "MG",
    "Rio de janeiro": "RJ",
    "Paraíba": "PB",
    "Paraiba": "PB",
    "Pernambuco": "PE"

}

def obter_dados_time():
    time = {}
    time["nome"] = (input("Qual o nome do time? ")).capitalize()
    tratar_estado = (input(f"Qual o estado do {time['nome']}? ")).capitalize()
    time["estado"] = dicionario_estados[tratar_estado]
    time["pontos"] = int(input(f"Qual a quantidade de pontos do {time['nome']}? "))
    return time


quant_times = int(input("Qual a quantidade de times a ser inserida no sistema? "))

# Obter dados de todos os times
times = []
for i in range(quant_times):
    times.append(obter_dados_time())

# Filtrar times por estado e pontuação
times_pe_pb_100 = list(filter(lambda time: (time["estado"] in ["PB", "PE"]) and (time["pontos"] > 100), times))
times_mg = list(filter(lambda time: time["estado"] == "MG", times))
times_rj = list(filter(lambda time: time["estado"] == "RJ", times))

# Calcular a soma e média dos pontos dos times do RJ
soma_pontos_rj = sum(time["pontos"] for time in times_rj)
media_pontos_rj = soma_pontos_rj / len(times_rj) if len(times_rj) > 0 else 0

# Encontrar o time com maior pontuação
time_maior_pontuacao = max(times, key=lambda time: time["pontos"], default=None)

# Imprimir resultados
print(f"Time com maior pontuação: {time_maior_pontuacao['nome']} ({time_maior_pontuacao['pontos']} pontos)")
print(f"Média de pontos dos times do RJ: {media_pontos_rj}")
if len(times_pe_pb_100) > 0:
    print(f"Times de PB e PE com mais de 100 pontos:")
    for time in times_pe_pb_100:
        print(f"  - {time['nome']} ({time['pontos']} pontos)")
else:
    print("Nenhum time da PB ou de PE foi fornecido")
if len(times_mg) > 0:
    print(f"Times de MG e suas pontuações:")
    for time in times_mg:
        print(f"  - {time['nome']} ({time['pontos']} pontos)")
else:
    print("Nenhum time de MG foi fornecido")