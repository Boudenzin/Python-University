contador = 0
pontuacao1 = 0
while (contador < 4):
    nome = input("Qual o seu nome?")
    pontuacao = int(input("Qual a sua pontuação? "))
    if (pontuacao > pontuacao1):
        pontuacao1 = pontuacao
        nomevencedor = nome
    contador +=1
    print (f"{nomevencedor} venceu a competição com {pontuacao1} pontos")
