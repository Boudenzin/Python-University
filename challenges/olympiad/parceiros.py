num = int(input())
nome1 = str.title(input())
nome2 = str.title(input())
nomes3 = []
nomes4 = []
nomes3.append(nome1)
nomes4.append(nome2)
z = []
for x in nome1:
    z.append(x)
nomes = []
index = 0
print (z)
for i in range(len(z)):
    if (z[i] == " "):
        print (z)
        nomes.append(z[index:i])
        index = i + 1
nomes.append(z[index:])
y = []
nomes2 = []
index = 0
for x in nome2:
    y.append(x)
for i in range(len(y)):
    if (z[i] == " "):
        print (y)
        nomes2.append(y[index:i])
        index = i + 1
nomes2.append(y[index:])
print (nomes)        
print (nomes2)

pares = []
for i in range(len(nomes)):
    pares.append([nomes[i],nomes2[i]])


print (pares)
pares2 = []
for i in range (len(pares)):

    pares2.append(pares[i])
pares2.reverse()
print (pares2)

print (pares2[-1])
for a in range (0,-(len(pares))):

    for i in range(len(pares)):
        if nomes[i] == nomes2[i]:
            result = "bad"
        elif pares[i] == pares2[a]:
            result = "good"
print (result)

#for i in range
#if (pares[i][0]):
        #result = "bad"



#for i in range (num):
    #for a in range (num):
        #pares 
    #if (nomes[i] == nomes2[i]):
        #result = "bad"