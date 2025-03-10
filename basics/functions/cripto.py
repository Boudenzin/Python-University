def codigoASCII (texto):
    #Função que funciona como uma cifra de cesar
    lista = []
    for i in range (len(texto)): #Recebe cada caractere da palavra, transforma em ASCII e soma +5
        codigo = ord(texto[i])
        codigo += 5
        lista.append(codigo)
    for i in range(len(lista)): #Agora ele faz o inverso, transforma cada codigo ASCII modificado e transforma em caractere
        codigo = chr(lista[i])
        lista[i] = codigo
    return lista

