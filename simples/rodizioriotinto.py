#Regras de Negócio
rodizio_gratis = 10

#Entrada de Dados
convidados = int(input("Quantos convidados você convidou para o seu aniversário? "))
preco_rodizio = float(input("Qual o preço do rodízio? "))

#Processamento de Dados
rodizio_gratis = convidados // rodizio_gratis
preco_total = (convidados - rodizio_gratis) * preco_rodizio

#Saída de Dados
print (f"O valor total a pagar será de R$ {preco_total:.2f}")
