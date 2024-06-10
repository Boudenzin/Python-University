
multa_ate_dois = 30.00
multa_ate_tres = 80.00
multa_maior_tres = 40.00

faixas_multa = {0: 0.00, 2: multa_ate_dois, 3: multa_ate_tres, float('inf'): multa_maior_tres}

diaria = float(input("Seja bem vind@ a nossa locadora, digite o valor da diária: "))
dias = int(input("Quantos dias você alugou o carro? "))

while True:
    try:
        tempo_atraso = int(input("Caso houver atraso na devolução, informar o valor em horas: "))
        if tempo_atraso < 0:
            raise ValueError("Tempo de atraso não pode ser negativo.")
        break
    except ValueError:
        print("Tempo de atraso inválido. Digite um número inteiro não negativo.")

valor_total = diaria * dias
multa = faixas_multa.get(tempo_atraso, multa_maior_tres) * tempo_atraso
valor_total += multa

if (tempo_atraso == 0):
    print(f"Já que não houve atraso, o valor a ser pago é equivalente a R$ {valor_total:.2f}")
else:
    print (f"Já que houve atraso, com multa de R$ {multa}, o valor a ser pago é R$ {valor_total:.2f}")


