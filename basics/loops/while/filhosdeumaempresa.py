#Regras de Negócio
qtdtotalfilhos = 0
qtdfuncionarios = 0
mediafilhos = 0
#Repetição que para quando é informado um número negativo
qtdfilhos = int(input("Quantos filhos você tem?"))
while (qtdfilhos > 0):
    qtdtotalfilhos += qtdfilhos
    qtdfuncionarios += 1
    mediafilhos = qtdtotalfilhos / qtdfuncionarios
    qtdfilhos = int(input("Quantos filhos você tem?"))
print (f"A média de filhos por funcionários é de {mediafilhos:.2f}")
#Cadastramento da média da quantidade de filhos por funcionário    