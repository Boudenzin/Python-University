#Entrada de Dados

revistas = int(input("Qual a quantidade total de revistas que você possui? "))
amigos = int(input("Para quantos amigos você irá querer doar as suas revistas? "))

#Processamento de Dados

revistas_por_amigos = revistas // amigos
revistas_restantes = revistas % amigos

#Saida de Dados
print (f"Você doará {revistas_por_amigos} revistas para cada pessoa e sobrarão {revistas_restantes} revistas")
