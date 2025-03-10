"""
#CÓDIGO ORIGINAL A BAIXO

habitantes_sudeste = []
soma_habitantes_sudeste = 0
dados_estados = []
estados_sul = []
estados_nordeste_100 = []
estados_centro_oeste = []
estados_norte = []
limite_habitantes_centrooeste = 500000

quant_estados = int(input("Qual a quantidade de estados que você quer inserir? "))

for i in range (quant_estados):
    nome = str.title(str.lower(input(f"Qual o nome do {i + 1}º estado: ")))
    regiao = str.title(str.lower(input(f"Qual a região do {i + 1}º estado: ")))
    quantmunicipios = int(input(f"Qual a quantidade de municipios desse estado? "))
    quanthabitantes = int(input(f"Qual a quantidade de habitantes desse estado: "))

    dados_estados.append([nome, regiao, quantmunicipios, quanthabitantes])


nomesdasregioes = ["Nordeste", "Norte", "Sul", "Centro-Oeste", "Sudeste"]

for i in range (quant_estados):
    if (dados_estados[i][1] == nomesdasregioes[2]):
        estados_sul.append(dados_estados[i][1])

for i in range (quant_estados):
    if (dados_estados[i][1] == nomesdasregioes[0]):
        if (quantmunicipios > 100):
            estados_nordeste_100.append(dados_estados[i][0])      

for i in range (quant_estados):
    if (dados_estados[i][1] == nomesdasregioes[1]):
        estados_norte.append(dados_estados[i][0])  

for i in range (quant_estados):
    if (dados_estados[i][1] == nomesdasregioes[3]):
        if (dados_estados[i][3] < limite_habitantes_centrooeste):
            estados_centro_oeste.append(dados_estados[i][0])

for i in range (quant_estados):
    if (dados_estados[i][1] == nomesdasregioes[4]):
        habitantes_sudeste.append(dados_estados[i][3])

for i in range (quant_estados):
    if (dados_estados[i][1] == nomesdasregioes[4]):
        soma_habitantes_sudeste += habitantes_sudeste[i]
media_dos_hab_do_sudeste = soma_habitantes_sudeste / (len(str(habitantes_sudeste)))

print (f"O nome dos estados da Região Sul: {estados_sul}")
print (f"A quantidade de Estados da Região Nordeste com mais de 100 municípios: {len(estados_nordeste_100)}")
print (f"A quantidade total de cidades dos Estados da Região Norte: {estados_norte}")
print (f"A quantidade de Estados da Região Centro-Oeste com menos de 500 mil habitantes: {habitantes_sudeste}")
print (f"A quantidade média de habitantes dos Estados da Região Sudeste: {media_dos_hab_do_sudeste}")

CÓDIGO ORIGINAL ACIMA"""

#CÓDIGO MELHORADO COM PANDAS

import pandas as pd

def obter_dados_estado():
    estado = {}
    estado["nome"] = str.title(str.lower(input("Qual o nome do estado: ")))
    estado["regiao"] = str.title(str.lower(input(f"Qual a região do estado {estado['nome']}: ")))
    estado["quantmunicipios"] = int(input(f"Qual a quantidade de municípios de {estado['nome']}: "))
    estado["quanthabitantes"] = int(input(f"Qual a quantidade de habitantes de {estado['nome']}: "))
    return estado


quant_estados = int(input("Qual a quantidade de estados que você quer inserir? "))

# Obter dados de todos os estados
dados_estados = []
for i in range(quant_estados):
    dados_estados.append(obter_dados_estado())

# Criar DataFrame a partir dos dados dos estados
df_estados = pd.DataFrame(dados_estados)

# Filtrar estados por região
estados_sul = df_estados[df_estados["regiao"] == "Sul"]["nome"].tolist()
estados_sudeste = df_estados[df_estados["regiao"] == "Sudeste"]["nome"].tolist()
estados_centro_oeste = df_estados[df_estados["regiao"] == "Centro-Oeste"]["nome"].tolist()
estados_norte = df_estados[df_estados["regiao"] == "Norte"]["nome"].tolist()
estados_nordeste_100 = df_estados[(df_estados["regiao"] == "Nordeste") & (df_estados["quantmunicipios"] > 100)]["nome"].tolist()


# Calcular a média de habitantes do Sudeste
habitantes_sudeste = df_estados[df_estados["regiao"] == "Sudeste"]["quanthabitantes"]
if len(habitantes_sudeste) > 0:
    media_dos_hab_do_sudeste = habitantes_sudeste.sum() / len(habitantes_sudeste)
else:
    media_dos_hab_do_sudeste = 0

# Imprimir resultados
print(f"O nome dos estados da Região Sul: {estados_sul}")
print(f"A quantidade de Estados da Região Nordeste com mais de 100 municípios: {len(estados_nordeste_100)}")
print(f"A quantidade total de cidades dos Estados da Região Norte: {df_estados[df_estados['regiao'] == 'Norte']['quantmunicipios'].sum()}")
print(f"A quantidade de Estados da Região Centro-Oeste com menos de 500 mil habitantes: {len(df_estados[(df_estados['regiao'] == 'Centro-Oeste') & (df_estados['quanthabitantes'] < 500000)])}")
print(f"A quantidade média de habitantes dos Estados da Região Sudeste: {media_dos_hab_do_sudeste}")


