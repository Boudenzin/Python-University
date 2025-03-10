produto = 1
qtdeNumeros = 0
while (qtdeNumeros < 5):
    numero = int (input("a: "))
    if (numero % 2 != 0) or (numero < 0):
        produto = numero * produto
    qtdeNumeros = qtdeNumeros + 1
print(produto)