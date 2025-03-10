tempo_minimo = 55
beneficio = 0.6
bonus = 0.15

tempo = int(input("Quanto tempo você já contribuiu para o INSS? "))
salario = float(input("Qual o seu salário atual? "))

if (tempo < tempo_minimo):
    print ("Não tem direito ao benefício")

else:
    totalpago = beneficio * salario
    if (tempo > tempo_minimo):
        bonustotal = bonus * (tempo - tempo_minimo)
        totalpago = totalpago + (salario * bonustotal)
    print (f"Você receberá R$ {totalpago:.2f}")
    
