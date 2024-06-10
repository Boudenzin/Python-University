#Regras de Negócio
imposto_mil = 0.17
imposto_menor_que_mil = 0.08


#Entrada de Dados
salario = float(input("Qual o valor do seu salário: "))

#Processamento de Dados e Saída de Dados

if (salario >=1000):
    imposto = salario * imposto_mil
else:
    imposto = salario * imposto_menor_que_mil


print ("O imposto a ser pago é R$ %.2f" % imposto)
