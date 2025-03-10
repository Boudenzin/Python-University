orcamento2017 = []
quantMeses = 3
mesesmaioresque2500 = []
somadasreceitas = 0
qtdereceitasmaioresqueadespesa = 0

for i in range(quantMeses):
    mes = input("Digite o mês: ")
    receita = float(input("Digite a receita do mês: "))
    despesa = float(input("Digite a despesa do mês: "))

    sublista = [mes, receita, despesa]

    orcamento2017.append(sublista)

#Exiba o total recebido nos 5 primeiros meses.
primeirosMeses = ["janeiro", "fevereiro", "março", "abril", "maio"]

totalRecebido = 0
mesmaiordespesa = orcamento2017[0][2]

for i in range(quantMeses):
    if (orcamento2017[i][0].lower() in primeirosMeses):
        totalRecebido += orcamento2017[i][1]
    if (orcamento2017[i][2] > 2500):
        mesesmaioresque2500.append(orcamento2017[i][0])
    if (orcamento2017[i][1] > orcamento2017[i][2]):
        qtdereceitasmaioresqueadespesa += 1
    if (orcamento2017[i][2] > mesmaiordespesa):
        mesmaiordespesa = orcamento2017[i][2]
    somadasreceitas += orcamento2017[i][1]
mediadasreceitas = somadasreceitas / quantMeses

print (f"O total recebido nos 5 primeiros meses foi de: {totalRecebido}")
print (f"Os meses em que as despesas foram maiores que 2500 foram: {mesesmaioresque2500}")
print (f"A quantidade de meses em que a receita foi maior que a despesa é {qtdereceitasmaioresqueadespesa}")
print (f"O mês que teve a maior despesa foi {mesmaiordespesa}")
print (f"A média das receitas é: {mediadasreceitas:.2f}")
