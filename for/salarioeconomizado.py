#Programa que calcula a economia mensal dos 3 primeiros meses


def get_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                raise ValueError("Valor inválido. Digite um número positivo.")
            return valor
        except ValueError:
            print("Valor inválido. Digite um número positivo.")

economia_total = 0

salario = get_valor("Qual o valor do seu salário? ")
for ordemdosmeses in range (1,4):
    despesas = get_valor(f"Qual a sua despesa no mês {ordemdosmeses}: ")
    economia = salario - despesas
    economia_total += economia
economia_total /= ordemdosmeses
print(f"Sua economia: R${economia_total:.2f}")
