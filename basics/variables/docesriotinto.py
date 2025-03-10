#Regras de Negócio
preco_beijinhos = 1.7
preco_brigadeiros = 1.9

#Entrada de Dados
brigadeiros = int(input("Olá! Quantos brigadeiros você irá querer? "))
beijinhos = int(input("Quantos beijinhos você irá querer? "))
criancas = int(input("Quantas crianças irão para a sua festa? "))

#Processamento de Dados
preco_total = (beijinhos * preco_beijinhos) + (brigadeiros * preco_brigadeiros)
doce_por_crianca = (beijinhos + brigadeiros) // criancas

#Saída de Dados
print (f"O total gasto será de R$ {preco_total:.2f} e teremos {doce_por_crianca} docinhos para cada criança")
