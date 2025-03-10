
precos = {
    "Relógio": {"Metal": 215.00, "Couro": 150.00},
    "Bolsa": {"Couro": 180.00, "Tecido": 100.00}

}

err_input = True

while err_input:
    try:
        presente = input("Que presente você irá comprar? (Relógio/Bolsa): ").capitalize()
        if presente not in precos:
            raise ValueError
        err_input = False
    except ValueError:
        print ("Opção de presente inválida. Digite 'Relógio' ou 'Bolsa'.")

err_input = True

while err_input:
    try:        
        material = input(f"Qual o material do {presente}? ({'/'.join(precos[presente].keys())}): ").capitalize()
        if material not in precos[presente]:
            raise ValueError(f"Opção de material de {presente} inválida")
        err_input = False
    except ValueError:
        print (f"Opção de material de {presente} inválida. Digite uma das opções demonstradas")


precototal = precos[presente][material]
print (f"O preço do {presente} de {material} ficará por {precototal}")

if (presente == "Relógio"):
    print ("Você acaba de ganhar um chaveiro de brinde na compra do seu relógio!")