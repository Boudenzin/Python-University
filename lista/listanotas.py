
quant_aprovados = 0
nota_minima = 8
notas = []

for i in range (5):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

for i in range (5):
    if (notas[i] >= nota_minima):
        quant_aprovados += 1

print (f"A quantidade de aprovados foi {quant_aprovados}")



