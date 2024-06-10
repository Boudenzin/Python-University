

import unicodedata



def testaVogal (letra):

    #Ignora se a vogal tem acento ou não
    normalized = unicodedata.normalize("NFD", letra)
    vowel = normalized.encode("ascii", "ignore").decode ("utf8").casefold()

    #Retorna um booleano se for vogal ou se não for vogal
    vogais = ["a","e","i","o","u"]
    if (vowel in vogais):
        return True
    return False

