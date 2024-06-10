#Programa que lista a quantidade de cachorros, o nome dos gatos, as idades do pássaros, nome dos
#animais com menos de 1 ano e a média de idade dos gatos

animais = []
quantCachorros = 0
nomesGatos = []
idadesPassaros = []
nomesMenos1 = []
somaGatos = 0

quantAnimais = int(input("Qual a quantidade de animais que você quer inserir no sistema? "))

for rep in range (quantAnimais):
    nome = str.title(input("Qual o nome do seu animal?"))
    idade = float(input("Qual a idade do seu animal?"))
    tipo = str.title(input("Qual o tipo do seu animal? "))
    animais.append([nome, idade, tipo])

for i in range (len(animais)):
    if (animais[i][2] == "Cachorro"):
        quantCachorros += 1

for i in range (len(animais)):
    if (animais[i][2] == "Gato"):
        nomesGatos.append(animais[i][0])
    
for i in range (len(animais)):
    if (animais[i][2] == "Pássaro"):
        idadesPassaros.append([animais[i][0],animais[i][1]])

for i in range (len(animais)):
    if ((animais[i][1]) < 1):
        nomesMenos1.append(animais[i][0])
        
for i in range (len(animais)):
    if (animais[i][2] == "Gato"):
        somaGatos += animais[i][1]
mediaGatos = somaGatos / len(nomesGatos)

print (f"A quantidade de cachorros é: {quantCachorros}")
print (f"O nome dos gatos são: {nomesGatos}")
print (f"As idades dos pássaros são {idadesPassaros}")
print (f"Os nomes dos animais com menos de um ano: {nomesMenos1}")
print (f"A média de idade dos gatos é {mediaGatos:.2f}")




