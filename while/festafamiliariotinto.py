execucao = "SIM"
pessoas = 0
dinheiroporpessoa = 14
while (execucao == "SIM"):
    familiares = int(input("Qual a quantidade de familiares que voce irá levar? "))
    pessoas = familiares + pessoas + 1
    execucao = str.upper(input("Deseja continuar? (Sim ou Não)"))
dinheirogasto = pessoas * dinheiroporpessoa  
print (f"Total de Pessoas: {pessoas}")
print (f"Dinheiro Gasto: {dinheirogasto}")

