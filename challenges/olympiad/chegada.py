#rush das 7 ate 10 da manha
#rush das 15 ate 19 da noite

#Ela sai na hora (XX:00), 20 minutos depois da hora (XX:20), ou 40 minutos depois da hora (XX:40)
hora = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
minuto = [":00", ":20", ":40"]

hora_rush = []
hora_rush.append(hora[7:11])
hora_rush.append(hora[15:20])

print (hora_rush)

tempo_saida = [str(input(""))]

hora_teste = tempo_saida[:2]
minuto_teste = tempo_saida[2:]
print (hora_teste)
for x in hora_rush:
    if (hora_teste[0] in x):
        if (hora_teste[0] == hora_)
