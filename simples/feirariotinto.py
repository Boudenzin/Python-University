#Regras de Negócio
preco_duzia = 9.75/12

#Entrada de Dados
laranjas = int(input("Olá! Quantas laranjas você deseja? "))

#Processamento de Dados
pagamento = preco_duzia * laranjas

#Saida de Dados
print (f"O preço total do seu pedido foi R$ {pagamento:.2f}")
