#Regras de Negócio
desconto = 0.95

#Entrada de Dados
print ("Olá seja bem vind@ ao nosso sistema!")
ipva = float(input("Qual o valor do seu IPVA? "))
taxa = float(input("Qual o valor da sua taxa de trânsito? "))

#Processamento de Dados
pagamento = (ipva * desconto) + taxa

#Saída de Dados
print (f"Segundo meus cálculos, você tem que pagar uma quantia equivalente a R$ {pagamento:.2f}")


