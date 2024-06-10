
multiplos_tres = []
numeros = []
for i in range (8):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for i in range (8):
    if (numeros[i] % 3 == 0):
        multiplos_tres.append(numeros[i])

print (multiplos_tres)