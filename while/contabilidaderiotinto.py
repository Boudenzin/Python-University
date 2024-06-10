#Regras de Negócio
somacredito = 0
somadebito = 0
qtdcredito = 0
tipo = "CRÉDITO"
#Repetição de Movimentações Monetárias envolvendo Crédito e Débito, com definição da palavra "SAIR" para terminar a repetição
while (tipo != "SAIR"):
    tipo = str.upper (input("Qual o tipo do valor? (CRÉDITO / DÉBITO / SAIR) "))
    if (tipo == "CRÉDITO"):
        valorcredito = float (input("Digite o valor da sua movimentação em crédito: "))
        #Acumulação da quantidade de crédito e acumulo de dinheiro gasto em crédito
        qtdcredito += 1
        somacredito += valorcredito
    elif (tipo == "DÉBITO"):
        valordebito = float (input("Digite o valor da sua movimentação em débito: "))
        #Acumulo de dinheiro gasto em débito
        somadebito += valordebito
#O saldo financeiro é calculado com o dinheiro gasto em crédito menos o dinheiro gasto em débito
saldofinanceiro = somacredito - somadebito
print (f"Quantidade de crédito: {qtdcredito}")
print (f"Saldo financeiro: {saldofinanceiro:.2f}")
#Teste para identificar se o saldo é positivo ou negativo
if (saldofinanceiro >= 0):
    resultadosaldofinanceiro = "Positivo"
else:
    resultadosaldofinanceiro = "Negativo"
print (f"Saldo {resultadosaldofinanceiro}")