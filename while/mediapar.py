contagem = 0
soma = 0
numero = int(input("Digite um número "))
while (numero != 100):
    if (numero % 2 == 0):
        contagem = contagem + 1 
        soma = soma + numero
    numero = int(input("Digite um número"))

media = soma / contagem
print (media)
    
        
        
        

