import random

soma_cinco_primeiros = 0
elementos_impares = 0
lista_aleatoria = [random.randint(0,10) for i in range(10)]



menor_elemento = lista_aleatoria[0]
for sum in range (5):
    soma_cinco_primeiros += lista_aleatoria[sum]
for min in range (1,9):
    if (lista_aleatoria[min] < menor_elemento):
        menor_elemento = lista_aleatoria[min]
for odd in range (9):
    if (lista_aleatoria[odd] % 2 != 0):
        elementos_impares += 1
        
print (lista_aleatoria)
print (f"Primeiro número: {lista_aleatoria[0]}. Segundo Número: {lista_aleatoria[9]}")
print (f"A soma dos cinco primeiros números é: {soma_cinco_primeiros}")
print (f"O menor elemento da lista é: {menor_elemento}")
print (f"A quantidade de elementos ímpares é de: {elementos_impares}")