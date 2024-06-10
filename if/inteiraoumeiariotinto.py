ingressovip = 350.00
ingressocadeira = 200.00
ingressoarquibancada = 100.00
meiaentrada = 0.5
taxaconveniencia = 0.05

setor = str.upper(input("Qual o setor que você irá participar e quer adquirir? "))
ingresso = str.upper(input("A entrada será meia ou inteira? "))

if ((setor == "ARQUIBANCADA") or (setor == "PLATEIA VIP") or (setor == "CADEIRA")):
    if (setor == "ARQUIBANCADA"):
        valoringresso = ingressoarquibancada
        
    elif (setor == "CADEIRA"):
        valoringresso = ingressocadeira
        
    elif (setor == "PLATEIA VIP"):
        valoringresso = ingressovip

    if (ingresso == "INTEIRA"):
        totalpago = valoringresso * taxaconveniencia
        totalpago = totalpago + valoringresso
        print (f"O valor a ser pago é de R$ {totalpago:.2f}")
    else:
        if (setor == "PLATEIA VIP"):
            print ("TIPO DE INGRESSO INVÁLIDO")
        else:
            totalpago = (valoringresso * meiaentrada) + (valoringresso * taxaconveniencia)
            print (f"O valor a ser pago é R$ {totalpago:.2f}")
else:
    print ("SETOR INVÁLIDO")



        


    
