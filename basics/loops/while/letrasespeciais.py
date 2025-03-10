contagem = 0
letra = str.upper(input("Digite uma letra: "))
while (letra != "X"):
    if (letra == "K"):
        contagem = contagem + 1
    elif (letra == "Y"):
        contagem = contagem + 1
    elif (letra == "W"):
        contagem = contagem + 1
    letra = str.upper(input("Digite uma letra: "))
print (contagem)

