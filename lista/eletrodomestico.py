def obter_dados_venda():
    venda = {}

    venda["tipo_produto"] = input("Digite o tipo de produto (Eletrodoméstico, Móvel ou Decoração): ").capitalize()
    while venda["tipo_produto"] not in tipos_produtos:
        venda["tipo_produto"] = input("Tipo de produto inválido. Digite novamente (Eletrodoméstico, Móvel ou Decoração): ").capitalize()

    if venda["tipo_produto"] == tipos_produtos[1]:
        venda["cor_movel"] = input("Qual a cor do móvel (Marfim ou Branco): ").capitalize()
        while venda["cor_movel"] not in cores_moveis:
            venda["cor_movel"] = input("Cor do móvel inválida. Digite novamente (Marfim ou Branco): ").capitalize()
    
    elif venda["tipo_produto"] == tipos_produtos[0]:
        venda["marca_eletrodomestico"] = input("Qual a marca do eletrodoméstico (Brastemp ou Electrolux): ").capitalize()
        while venda["marca_eletrodomestico"] not in tipos_eletrodomesticos:
            venda["marca_eletrodomestico"] = input(f"Marca de eletrodoméstico inválida. Digite novamente ({tipos_eletrodomesticos}): ").capitalize()
    
    elif venda["tipo_produto"] == tipos_produtos[2]:
        venda["descricao_decoracao"] = input("Qual a descrição da decoração: ").capitalize()
    venda["preco_decoracao"] = int(input("Qual o preço do produto: R$"))

    return venda

#Declaração de Inputs que podem ser colocados
tipos_produtos = ["Eletrodoméstico", "Móvel", "Decoração"]
tipos_eletrodomesticos = ["Brastemp", "Electrolux"]
cores_moveis = ["Marfim", "Branco"]

quant_vendas = int(input("Qual a quantidade de vendas: "))

# Obter dados de todas as vendas
vendas = []
for i in range(quant_vendas):
    vendas.append(obter_dados_venda())

# Contar vendas por tipo de produto
quant_vendas_movel = sum(1 for venda in vendas if venda["tipo_produto"] == tipos_produtos[1])
quant_vendas_eletrodomestico = sum(1 for venda in vendas if venda["tipo_produto"] == tipos_produtos[0])
quant_vendas_decoracao = sum(1 for venda in vendas if venda["tipo_produto"] == tipos_produtos[2])

# Contar vendas por cor de móvel
quant_vendas_movel_marfim = sum(1 for venda in vendas if venda["tipo_produto"] == tipos_produtos[1] and venda["cor_movel"] == cores_moveis[0])
quant_vendas_movel_branco = sum(1 for venda in vendas if venda["tipo_produto"] == tipos_produtos[1] and venda["cor_movel"] == cores_moveis[1])

# Contar vendas por marca de eletrodoméstico
quant_vendas_brastemp = sum(1 for venda in vendas if venda["tipo_produto"] == tipos_produtos[0] and venda["marca_eletrodomestico"] == tipos_eletrodomesticos[0])
quant_vendas_electrolux = sum(1 for venda in vendas if venda["tipo_produto"] == tipos_produtos[0] and venda["marca_eletrodomestico"] == tipos_eletrodomesticos[1])

#Calcular a porcentagem das vendas das cores dos móveis
if quant_vendas_movel > 0:
    percentual_marfim = (quant_vendas_movel_marfim / quant_vendas_movel) * 100
    percentual_branco = 100 - percentual_marfim
else:
    quant_vendas_movel = 0
    percentual_marfim = 0
    percentual_branco = 0

# Calcular preços médios
preco_total_decoracao = sum(venda["preco_decoracao"] for venda in vendas if venda["tipo_produto"] == tipos_produtos[2])
if preco_total_decoracao > 0:
    preco_medio_decoracao = preco_total_decoracao / quant_vendas_decoracao
else:
    preco_medio_decoracao = 0.00

# Identificar o eletrodoméstico mais vendido
if quant_vendas_eletrodomestico > 0:
    eletrodomestico_mais_vendido = tipos_eletrodomesticos[0] if quant_vendas_brastemp > quant_vendas_electrolux else tipos_eletrodomesticos[1]
    eletrodomestico_mais_vendido = "Empate entre ambas as marcas" if quant_vendas_brastemp == quant_vendas_electrolux else eletrodomestico_mais_vendido
else:
    quant_vendas_eletrodomestico = 0

# Saída dos Dados
print(f"Percentuais de móveis vendidos: {tipos_produtos[0]} = {percentual_marfim}%. {tipos_produtos[1]} = {percentual_branco}%")
print(f"Preço médio de decorações vendidas: R${preco_medio_decoracao}")
print(f"Resultado do eletrodoméstico mais vendido: {eletrodomestico_mais_vendido}")
