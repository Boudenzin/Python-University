
N = int(input())
for i in range(N):
    nova_palavra = []
    palavra_embaralhada = input()
    for i in range (len(palavra_embaralhada)):
        nova_palavra.append(palavra_embaralhada[i])
    comprimento = len(nova_palavra)
    cut = comprimento//2
    invertido = palavra_embaralhada[::-1]
    pedaco1 = invertido[cut:]
    pedaco2 = invertido[:cut]
    palavra_original = pedaco1+pedaco2
    print (palavra_original)
