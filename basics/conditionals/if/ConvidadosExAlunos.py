taxa_ex_aluno = 60.00
convidados_12_mais = 50
convidados_3a11_anos = 25
convidados_menos_3 = 0

participante = str.upper(input("Qual o tipo do participante? "))

if (participante == "EX-ALUNO"):
    total_pago = taxa_ex_aluno
else:
    idade = int(input("Qual a idade do convidado? "))
    if (idade >= 12):
        total_pago = convidados_12_mais
    elif (idade > 3):
        total_pago = convidados_3a11_anos
    else:
        total_pago = convidados_menos_3

print (f"O valor total a ser pago é de R$ {total_pago:.2f}")
        
