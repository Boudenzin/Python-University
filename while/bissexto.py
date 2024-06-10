contagem = 0
ano = int(input("Digite um ano: "))
while (ano >=0):
    if (ano % 400 == 0):
        contagem = contagem + 1
        print (f"{ano} é bissexto")
    elif (ano % 4 == 0) and (ano % 100 != 0):
        contagem = contagem + 1
        print (f"{ano} é bissexto")
    ano = int(input("Digite um ano: "))

print (contagem)
