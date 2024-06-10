from BibNumeros import testaMultiplo4

numeros = []

for i in range (5):
    n = int(input())
    numeros.append(n)
 
quantMultiplo4 = 0
for i in numeros:
    testaMultiplo4(i)
    if (testaMultiplo4(i) == True):
        quantMultiplo4 += 1
print (quantMultiplo4)

