#Regras de Negócio
preco_convenio = 170
preco_particular = 310

#Entrada de Dados
quant_convenio = float(input("Olá! Quantas consultas realizadas por convênio você realizou? "))
quant_particular = float(input("Quantas consultas particulares você realizou? "))

#Processamento de Dados
preco_total = (quant_convenio * preco_convenio) + (quant_particular * preco_particular)

#Saida de Dados
print (f"O valor a receber será R$ {preco_total:.2f}")
