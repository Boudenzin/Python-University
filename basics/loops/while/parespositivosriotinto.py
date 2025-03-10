contador = 0
qtdpositivoepar = 0
while (contador < 5):
    numero = int(input("Digite um número: "))
    if (numero % 2 == 0) and (numero >= 0):
        qtdpositivoepar +=1
    contador +=1
print (f"A quantidade de números pares e positivos é {qtdpositivoepar}")
