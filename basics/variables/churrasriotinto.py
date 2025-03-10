#Regras de Negócio
latas_por_pessoa = 6
carne_por_pessoa = 0.4
preco_quilo = 41
preco_cerveja = 5.2

#Entrada de Dados
pessoas = int(input("Quantas pessoas aceitaram o convite do seu churras? "))

#Processamento de Dados
carne = (carne_por_pessoa * pessoas) * preco_quilo
cerveja = (latas_por_pessoa * pessoas) * preco_cerveja

#Saída de Dados
print (f"Você gastará R$ {carne:.2f} com carne")
print (f"Você também gastará R$ {cerveja:.2f} com cerveja, boa sorte")

