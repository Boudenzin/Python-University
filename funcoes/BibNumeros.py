def contaDivisores(inteiro):
  quantDivisores = 0
  for i in range (1,(inteiro + 1)):
    if (inteiro % i == 0):
      quantDivisores += 1
  return quantDivisores


def testaMultiplo4 (inteiro):
  if (inteiro % 4 == 0):
    return True
  return False

