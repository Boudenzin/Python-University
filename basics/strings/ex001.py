def ContaVogais (palavra):
    quantVogais = 0
    vogais = ["a","e","i","o","u"]
    for x in palavra:
        if x.lower() in vogais:
            quantVogais += 1
    return quantVogais


def ProcuraS (palavra):
    for x in palavra:
        if x.lower() == "s":
            return True
    return False

def RemoveA (palavra):
    novaPalavra = ""
    for x in palavra:
        if x.lower() != "a":
            novaPalavra += x
    return novaPalavra

def Inverte (palavra):
    novaPalavra = ""
    for x in palavra:
        novaPalavra = x + novaPalavra
    return novaPalavra

def QtdePontuacao (texto):
    quantSimbolos = 0
    simbolos = [".",",",";",":","!","?"]
    for x in texto:
        if (x.lower() in simbolos):
            quantSimbolos += 1
    return quantSimbolos

def RemoveLetras (texto):
    novaPalavra = ""
    letrasProibidas = ["k","w","y"]
    for x in texto:
        if x.lower() not in letrasProibidas:
            novaPalavra += x
    return novaPalavra

def TestaPalindromo (palavra):
    if (palavra.lower()) == Inverte(palavra).lower():
        return True
    return False

def Sobrenome (nome):
    i = 0
    while nome[i] != " ":
        i += 1
    inicio = i + 1
    i += 1
    while nome[i] != " ":
        i += 1
    final = i
    Sobrenome = nome[inicio:final]
    return Sobrenome

def Nome (nome):
    i = 0
    while nome[i] != " ":
        i += 1
    primeiroNome = nome[:i]
    return primeiroNome