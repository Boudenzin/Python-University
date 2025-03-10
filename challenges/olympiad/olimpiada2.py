#dia 1 = D reais
#31 x D reais
#dia 2 = D + 2 * A reais
# > 16 não aumenta mais
#dia 2 = 30 * (D + A)
#dia 3 = 29 * (D + 2 * A)
meses = 32
limite_diaria = 15
D = int(input("Qual o valor da diária? "))
A = int(input("Qual o aumento?"))
N = int(input("Qual o dia de chegada do hotel? "))

for i in range (meses):
    if (N > limite_diaria):
        total = D + A * (limite_diaria-1)
        total *= (meses - N)
    if (N == i):
        total = D + A * (N - 1)
        total *= (meses - N)
    
print (total)