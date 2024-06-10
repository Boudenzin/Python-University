# Programa que indica o preço médio das doações para cada idoso

doacao_arrecadada = 0
qtd_idosos = 0

continuar = True

while continuar:
    try:
        qtd_idosos = int(input("Qual a quantidade de idosos? "))
        if qtd_idosos <= 0:
            raise ValueError("Quantidade de idosos deve ser maior que zero.")
        break
    except ValueError:
        print("Valor inválido. Digite um número inteiro positivo.")

while continuar:
    try:
        doacao = float(input("Qual o valor que você quer doar? "))
        if doacao <= 0:
            raise ValueError("Valor da doação deve ser maior que zero.")
        break
    except ValueError:
        print("Valor inválido. Digite um número positivo.")

valor_por_idoso = doacao / qtd_idosos

print(f"Valor médio por idoso: R${valor_por_idoso:.2f}")
print(f"Valor doado por você: R${doacao:.2f}")
