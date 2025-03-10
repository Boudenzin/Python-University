precos = {
    "CELULAR": {"SAMSUNG": 879.18, "MOTOROLA": 921.40},
    "TABLET": {"MULTILASER": 339.50, "SAMSUNG": 417.22}
}

err_input = True

while err_input:
    try:
        aparelho = str.upper(input("Qual o tipo de aparelho que você quer? (CELULAR/TABLET): "))
        if aparelho not in precos:
            raise ValueError("Opção de aparelho inválida.")
        err_input = False
    except ValueError:
        print("Opção de aparelho inválida. Digite 'CELULAR' ou 'TABLET'.")

err_input = True

while err_input:
    try:
        modelo = str.upper(input(f"Qual o modelo de {aparelho} que você irá querer? ({'/'.join(precos[aparelho].keys())}): "))
        if modelo not in precos[aparelho]:
            raise ValueError(f"Opção de modelo de {aparelho} inválida.")
        err_input = False
    except ValueError:
        print(f"Opção de modelo de {aparelho} inválida. Digite uma das opções disponíveis.")

err_input = True

while err_input:
    try:
        quantidade = int(input("Qual a quantidade desejada? "))
        if quantidade <= 0:
            raise ValueError("Quantidade inválida. Digite um número inteiro positivo.")
        err_input = False
    except ValueError:
        print("Quantidade inválida. Digite um número inteiro positivo.")

precototal = precos[aparelho][modelo] * quantidade
print(f"O valor total a ser pago é R$ {precototal:.2f}")

    

