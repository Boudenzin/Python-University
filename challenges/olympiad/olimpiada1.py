idades = []



for i in range (2):
    idade = int(input("Qual a sua idade? "))
    idades.append(idade)

somapreco = 0

for idade_teste in idades:
    if (idade_teste <= 17):
        preco = 15
    elif (idade_teste >= 60):
        preco = 20
    else:
        preco = 30
    somapreco += preco
print (somapreco)