execucao = "SIM"
idadecrianca = 10
idadeidoso = 60
totalentrada = 0
while (execucao == "SIM"):
    idade = int(input("Qual a sua idade?"))
    if (idade <= idadecrianca) or (idade > idadeidoso):
        totalentrada += 1

    execucao = str.upper(input("Deseja continuar? (Sim ou Não)"))

print (f"Total de entradas gratuitas: {totalentrada}")
