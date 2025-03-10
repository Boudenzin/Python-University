import random
import datetime
import pandas as pd

# Dicionários com dados fictícios
tipos_imoveis = {"Casa": 0.3, "Apartamento": 0.4, "Chácara": 0.2, "Sítio": 0.1}
quant_quartos = [2, 3, 4, 5]
tipos_negocio = {"Venda": 0.7, "Aluguel": 0.3}
faixas_preco = [(100000, 300000), (300000, 500000), (500000, 1000000)]
nomes = ["Alice Mendonça", "Pedro da Silva", "Carlos Zagetti", "Diana Francesca", "Juliano Otávio", "Fernanda Rodrigues", "Gustavo Félix", "Helena de Souza", "Isabel de Freitas", "João do Porto"]

# Geração de dados aleatórios
random.seed(123)  # Defina uma seed para reproduzir resultados consistentes
data_imoveis = []
for i in range(30):
    tipo_imovel = random.choices(list(tipos_imoveis.keys()), weights=list(tipos_imoveis.values()))[0]
    quartos = random.choice(quant_quartos)
    tipo_negocio = random.choices(list(tipos_negocio.keys()), weights=list(tipos_negocio.values()))[0]
    faixa_preco_min, faixa_preco_max = random.choice(faixas_preco)
    preco = random.randint(faixa_preco_min, faixa_preco_max)
    data_venda = datetime.date.today() - datetime.timedelta(days=random.randint(0, 365))
    nome_dono = random.choice(nomes)
    telefone = random.randint(100000000, 999999999)
    data_imoveis.append({
        "Tipo Imóvel": tipo_imovel,
        "Quartos": quartos,
        "Tipo Negócio": tipo_negocio,
        "Preço": preco,
        "Data Venda": data_venda,
        "Nome Dono": nome_dono,
        "Telefone": telefone
    })

# Criação do DataFrame
df_imoveis = pd.DataFrame(data_imoveis)

# Respostas às perguntas

# 1. Preços dos imóveis para aluguel
precos_aluguel = df_imoveis[df_imoveis["Tipo Negócio"] == "Aluguel"]["Preço"].tolist()
print(f"Os preços dos imóveis para aluguel são: {precos_aluguel}")

# 2. Dados dos donos com imóveis de 3 ou mais quartos
dados_donos_3_quartos = df_imoveis[df_imoveis["Quartos"] >= 3][["Nome Dono", "Preço", "Telefone"]]
print(f"Vendedores que contém 3 ou mais quartos para venda: \n {dados_donos_3_quartos}")

# 3. Média de preços oferecida pelo vendedor Juliano Otávio
precos_juliano = df_imoveis[df_imoveis["Nome Dono"] == "Juliano Otávio"]["Preço"].tolist()
media_precos_juliano = sum(precos_juliano) / len(precos_juliano)
print(f"Média de preços oferecida pelo vendedor Juliano Otávio: R${media_precos_juliano}")