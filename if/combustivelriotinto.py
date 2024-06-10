#Regras de Negócio

litrogasolina = 2.53
litroetanol = 2.09
litrodiesel = 1.92

#Entrada de Dados

combustivel = input("Bem vindo ao posto Abasteça! Qual o tipo de combustível desejado? ").capitalize()
dinheiro = float(input("Quanto dinheiro você deseja gastar? "))

#Processamento de Dados e Saída

if (combustivel == "Gasolina"):
    litro = dinheiro / litrogasolina
    print (f"Você acaba de abastecer seu carro com {litro:.2f} litros, mas não ganhou a troca de óleo")
    
elif (combustivel == "Etanol"):
    litro = dinheiro / litroetanol
    print (f"Você acaba de abastecer seu carro com {litro:.2f} litros")
    
    if (litro > 30):
        print ("Você ganhou uma troca de óleo!!")
        
    else:
        print ("Infelizmente, você não ganhou uma troca de óleo")
        
else:
     litro = dinheiro / litrodiesel
     print (f"Você acaba de abastecer seu carro com {litro:.2f} litros")
     
    
    
