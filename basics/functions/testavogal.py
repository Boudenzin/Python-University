from BibLetras import testaVogal

letras = []
for i in range(6):
    l = str(input())
    letras.append(l)

quantVogal = 0
for i in range (6):
    if (testaVogal(letras[i]) == True):
        quantVogal += 1

print (quantVogal)