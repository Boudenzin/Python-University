#Base de Dados
funcionarios_hotel = [ [ "Guilherme Sá", 26, "Segurança", 852.30 ],[ "Laura Dias", 31, "Recepção", 715.00 ],[ "Sônia Lopes", 44, "Lavanderia", 807.90 ],[ "Roberto Reis", 22, "Garagem", 475.69 ] ]

#Teste de alteração da Base de Dados
funcionarios_hotel[1][3] = 950.14
funcionarios_hotel.append(["Anísio Nunes", 38, "Garagem", 760.00])

#Aumento de 10% no salário do setor de Lavanderia
for i in range(len(funcionarios_hotel)):
    if (funcionarios_hotel[i][2].title() == "Lavanderia"):
      funcionarios_hotel[i][3] = funcionarios_hotel[i][3]*1.1  

#Funcionários com a idade menor que 30 anos (exibição apenas de nome e setor)
funcionarios_menor_30 = []
for i in range(len(funcionarios_hotel)):
    if (funcionarios_hotel[i][1] < 30):
        funcionarios_menor_30.append([funcionarios_hotel[i][0], funcionarios_hotel[i][2]])

#Funcionários que trabalham no setor de Lavanderia
cargo_lavanderia = []
for i in range(len(funcionarios_hotel)):
    if (funcionarios_hotel[i][2].title() == "Lavanderia"):
        cargo_lavanderia.append(funcionarios_hotel[i][0])

#Média de idade das pessoas que trabalham no setor Garagem
soma__idade_garagem = 0
quant_pessoas_garagem = 0
for i in range(len(funcionarios_hotel)):
    if (funcionarios_hotel[i][2].title() == "Garagem"):
        soma__idade_garagem += funcionarios_hotel[i][1]
        quant_pessoas_garagem += 1
media_idade_garagem = soma__idade_garagem / quant_pessoas_garagem

#Funcionário que ganha o maior salário
maior_salario = funcionarios_hotel[0][3] 
for i in range(len(funcionarios_hotel)):
    if (maior_salario < funcionarios_hotel[i][3]):
        maior_salario = funcionarios_hotel[i][3] 
        maior_nome = funcionarios_hotel[i][0]    

#Funcionário mais velho
mais_velho = funcionarios_hotel[0][1]
for i in range(len(funcionarios_hotel)):
    if (funcionarios_hotel[i][1] > mais_velho):
        mais_velho = funcionarios_hotel[i][1]
        setor_velho = funcionarios_hotel[i][2]

#Média salarial dos funcionários
soma_salarios = 0
for i in range(len(funcionarios_hotel)):
    soma_salarios += funcionarios_hotel[i][3]
media_salarios = soma_salarios / len(funcionarios_hotel)

#Salários acima da média
acima_salario = []
for i in range (len(funcionarios_hotel)):
    if(funcionarios_hotel[i][3] > media_salarios):
        acima_salario.append(funcionarios_hotel[i][0])
        
#Print dos Dados
print (funcionarios_hotel)

print (funcionarios_hotel[2][1], funcionarios_hotel[2][3])

print (funcionarios_menor_30)

print (cargo_lavanderia)

print (media_idade_garagem)

print (maior_nome)

print (setor_velho)

print (acima_salario)