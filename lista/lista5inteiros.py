#Dentre 5 números, verificará qual número será o menor (espera-se que o usuário digite ao menos algum número)
numeros = []

for count in range (5):
    numerosteste = numeros.append(int(input("Digite um número: ")))

menor = numeros[0]

for i in range (1,5):
    if (numeros[i] < menor):
        menor = numeros[i]

print (menor)