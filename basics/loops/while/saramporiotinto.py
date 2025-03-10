execucao = "SIM"
vacinas = 0
while (execucao != "NÃO"):
    idade = int(input("Qual a sua idade? "))
    if(idade>=3) and (idade<=6):
        vacinas += 1
    execucao = str.upper(input("Deseja continuar? (Sim ou Não)"))
print (f"Total de vacinas feitas: {vacinas}")
