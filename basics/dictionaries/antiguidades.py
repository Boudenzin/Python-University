def calcularItens1827(itens):

    itens1827 = 0
    for item in itens:
        if item['ano'] < 1827:
            itens1827 += 1
    return itens1827

def calcularValorMedio(itens):

    total = 0
    for item in itens:
        total += item['valor']
    return total / len(itens)

def encontrarPecaMaisValiosa(itens):

    pecaMaisValiosa = None
    for item in itens:
        if pecaMaisValiosa is None or item['valor'] > pecaMaisValiosa['valor']:
            pecaMaisValiosa = item
    return pecaMaisValiosa

# Cadastro dos itens
itens = []
for i in range(int(input("Quantos itens serão cadastrados: "))):
    descricao = str.title(str.lower(input("Qual a descrição da peça: ")))
    valor = float(input("Qual o valor da peça: "))
    ano = int(input("Qual o ano da peça: "))
    itens.append({'descricao': descricao, 'valor': valor, 'ano': ano})

# Cálculo dos resultados
itens1827 = calcularItens1827(itens)
valorMedio = calcularValorMedio(itens)
pecaMaisValiosa = encontrarPecaMaisValiosa(itens)

# Apresentação dos resultados
print(f"Itens produzidos antes de 1827: {itens1827}")
print(f"Valor médio dos itens: R$ {valorMedio}")
print(f"Dados do objeto mais valioso: {pecaMaisValiosa['descricao']}, {pecaMaisValiosa['ano']}")
