contadoraluno = 0
contadoraprovado = 0
somadasmedias = 0
mediamaior = 0
contadormaximoaluno = 4
contadormaximonota = 4
mediadeaprovacao
while (contadoraluno < contadormaximoaluno):
    soma= 0
    contadornota = 0
    while (contadornota < contadormaximonota):
        nota = float(input(f"Qual a {contadornota + 1}º nota do {contadoraluno + 1}º aluno? "))
        soma = nota + soma
        contadornota += 1
    media = soma / contadornota
    somadasmedias += media
    if (media >= mediadeaprovacao):
        resultado = "aprovado"
        contadoraprovado += 1
    else:
        resultado = "reprovado"
    if (media > mediamaior):
        mediamaior = media
    print (f"O aluno teve média {media:.2f} e foi {resultado}")
    contadoraluno += 1

mediaturma = somadasmedias / contadoraluno
print (f"Alunos aprovados: {contadoraprovado}")
print (f"Média da Turma: {mediaturma:.2f}")
print (f"Maior Média Obtida: {mediamaior}")
    
    
    
