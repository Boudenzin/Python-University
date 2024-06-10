#Regras de Negócio
expediente = 480 #em minutos

#Entrada de Dados
tempoprocesso = int(input("Quantos minutos você leva para analisar cada projeto? "))

#Processamento de Dados
processo = expediente // tempoprocesso

#Saída de Dados
print (f"Você conseguirá analisar {processo} processos por dia")
