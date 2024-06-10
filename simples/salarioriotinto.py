#Entrada De Dados
hora_aula = int(input("Quantas horas você trabalhou nesse mês: "))
projeto = int(input("De quantos projetos você participou esse mês: "))

#Processamento de Dados
salario = (hora_aula * 35) + (projeto * 80)

#Saída De Dados
print (f"O seu salário nesse momento é equivalente a: {salario:.2f} reais")
