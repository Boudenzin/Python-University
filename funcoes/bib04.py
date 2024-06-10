def MediaInteiraLista (lista: int) -> int:
    try:

        soma = 0
        for i in range (len(lista)):
            soma += lista[i]
        media = soma // len(lista)
        return media
    except Exception as error:
        return error


def MultiplicaLista (lista, valor):
    for i in range (len(lista)):
        lista[i] *= valor
    return lista
        
    
lista = []

def Busca (lista, valor):
    
    if (valor in lista):
        return True
    else:
        return False

def ContaOcorrências (lista, valor):
    encontrar = 0
    for i in range (len(lista)):
        if (valor == lista[i]):
            encontrar += 1
        return encontrar
    
def RemoveValor(lista, valor):
    novalista = []
    for i in range (len(lista)):
        if (valor != lista[i]):
            novalista.append(lista[i])
            
    return novalista


def SemRepeticao (lista):
    novalista = []
    for i in range (len(lista)):
        if (lista[i] not in novalista):
            novalista.append(lista[i])
    return novalista


def TestaOrdenacao (lista):
    if (lista != []):
        menor = lista[0]
        for i in range (1,len(lista)):
            if (lista [i] > menor):
                menor = lista[i]
            else:
                return False
    return True
        
print (TestaOrdenacao(lista))        

