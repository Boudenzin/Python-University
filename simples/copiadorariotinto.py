#Regras de Negócio
preco_pagina = 0.3

#Entrada de Dados
folhas = int(input("Quantas folhas você irá querer imprimir: "))

#Processamento de Dados
pagamento = (folhas * preco_pagina)

#Saida de Dados
print (f"O valor cobrado pelas {folhas} folhas, vale R$ {pagamento:.2f}")
