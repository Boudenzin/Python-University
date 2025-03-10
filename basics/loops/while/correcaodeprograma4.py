qtdeNumeros = 0
mult2 = 0
mult3 = 0
mult5 = 0
while (qtdeNumeros < 10):
    numero = int (input())
    if (numero % 2 == 0):
        mult2 = mult2 + numero
    elif (numero % 3 == 0):
        mult3 = mult3 + numero
    elif (numero % 5 == 0):
        mult5 = mult5 + numero
    qtdeNumeros = qtdeNumeros + 1 
print(mult2, mult3, mult5)