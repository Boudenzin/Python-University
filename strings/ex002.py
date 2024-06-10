def contaPalavras (texto):
    quantPalavras = 1
    for x in texto:
        if x == " ":
            quantPalavras += 1
    return quantPalavras

lista = ["Amanda", "Irineu", "Catarina", "Elisângela"]
def contaInicioVogal (lista):
    vogais = ["a","e","i","o","u"]
    quantVogais = 0
    for x in lista:
        if x[0].lower() in vogais:
            quantVogais += 1
    return quantVogais

