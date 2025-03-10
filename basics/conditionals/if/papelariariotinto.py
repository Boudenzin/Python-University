xeroxpb = 0.06
xeroxcolor = 0.29
encadernacao100 = 2.00
encadernacao101 = 4.00


msg = "Seja bem vindo a Papelaria Rio Tinto!"
print(msg)
servico = input("Temos xerox e encadernação disponivéis. Qual serviço você irá querer? : ").capitalize

if (servico == "Xérox" or servico == "Xerox"):
    tipodexerox = input("Ok, a Xérox será PB ou Colorida? ")
    
    if (tipodexerox == "PB"):
        paginas = int(input("Ok, qual a quantidade de páginas a serem xerocadas? : "))
        xeroxpb = xeroxpb * paginas
        print (f"Você terá que pagar R$ {xeroxpb:.2f}")
        
    elif (tipodexerox == "Colorida"):
        paginas = int(input("Ok, qual a quantidade de páginas a serem xerocadas? : "))
        xeroxcolor = xeroxcolor * paginas
        print (f"Você terá que pagar R$ {xeroxcolor:.2f}")
        
elif (servico == "Encadernação"):
    folhas = int(input("Ok, quantas folhas você quer encadernar? "))

    if (folhas<=100):
        print (f"Você terá que pagar R$ {encadernacao100:.2f}")

    else:
        print (f"Você terá que pagar R$ {encadernacao101:.2f}")
        
    