qtdeNumeros = 30
qtdePositivos = 0
numero = int (input("a: "))
while (qtdeNumeros > 0):
    if (numero >= 0):
        qtdePositivos = qtdePositivos + 1
    qtdeNumeros = qtdeNumeros - 1
    numero = int (input("a: "))
print(qtdePositivos)