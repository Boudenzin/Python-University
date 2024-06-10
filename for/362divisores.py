def encontrarDivisores(numero):

  divisores = []
  for testeDivisor in range(1, numero + 1):
    if numero % testeDivisor == 0:
      divisores.append(testeDivisor)
  return divisores

numero = int(input("Digite o número que você quer saber os seus divisores: "))
divisores = encontrarDivisores(numero)

print(f"O número {numero} tem {len(divisores)} divisores: \n{divisores}")
