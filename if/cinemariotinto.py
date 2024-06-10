"""preco2d = 8.50
preco3d = 14.50
combosimples = 10.00
combocompleto = 12.00

filme = input("O filme será 3D ou 2D? ")
resposta = input("Temos o COMBO SIMPLES, com refri e pipoca, e temos o COMBO COMPLETO que tem refri, pipoca e chocolate. Vai querer um deles? (S/N) : ")

if (filme == "2D"):
    valortotal = preco2d

else:
    valortotal = preco3d

if (resposta == "S"):
    lanche = input("Combo Simples ou Combo Completo? ")
    
    if (lanche == "Combo Simples"):
        valortotal = valortotal + combosimples
        
    else:
        valortotal = valortotal + combocompleto

print (f"O valor total do seu pedido é R$ {valortotal}")
"""

preco_2d = 8.50
preco_3d = 14.50
combo_simples = 10.00
combo_completo = 12.00

err_input = True


while err_input:  # Loop para validação de entrada do filme
    filme = input("O filme será 3D ou 2D? ").upper()
    if filme in ("2D", "3D"):
        err_input = False
    else:
        print("Opção inválida. Digite '2D' ou '3D'.")


valor_total = preco_3d if filme == "3D" else preco_2d

err_input = True

while err_input:  # Loop para validação de entrada da resposta
    resposta = input("Temos o COMBO SIMPLES, com refri e pipoca, e temos o COMBO COMPLETO que tem refri, pipoca e chocolate. Vai querer um deles? (S/N) : ").upper()
    if resposta in ("S", "N"):
        err_input = False
    else:
        print("Opção inválida. Digite 'S' ou 'N'.")

err_input = True

if resposta == "S":
    while err_input:  # Loop para validação de entrada do combo
        lanche = input("Combo Simples ou Combo Completo? ").upper()
        if lanche in ("COMBO SIMPLES", "COMBO COMPLETO"):
            break
        else:
            print("Opção inválida. Digite 'Combo Simples' ou 'Combo Completo'.")

    valor_total += combo_simples if lanche == "COMBO SIMPLES" else combo_completo

print(f"O valor total do seu pedido é R$ {valor_total:.2f}")  # Formatação de valor com 2 casas decimais


    
