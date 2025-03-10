#Regras de Negócio
precocriancas = 5.00
precoidosos = 15.00
precodemaior = 25.00

#Entrada de Dados
idade = int(input("Bem vindo ao Circo Desmantelo! Qual a sua idade, não permitimos menores de 0 anos: "))

#Processamento de Dados
if (idade>=60):
    preco = precoidosos
elif (idade<=5):
    preco = precocriancas
else:
    preco = precodemaior

print (f"Pague R$ {preco} ao banco")
