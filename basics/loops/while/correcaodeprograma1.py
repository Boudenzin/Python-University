qtdeNumeros = 20
soma = 0
while (qtdeNumeros > 0):
    numero = int (input("a: "))
    if (numero % 2 == 0):
        soma = soma + numero
    qtdeNumeros = qtdeNumeros - 1
print(soma)