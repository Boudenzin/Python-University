qtdaprovados = 0
questoesmat = 35
questoesport = 50
notaminimared = 7
porcentminimamat = 0.6
porcentminimaport = 0.8
notaderedacao = 0
notadematematica = 0
notadeportugues = 0

while (notadeportugues >= 0):
    notadeportugues = float(input("Qual a sua nota em português? "))
    if (notadeportugues >= 0):
        notadematematica = float(input("Qual a sua nota em matemática? "))
        notaderedacao = float(input("Qual a nota da sua redação? "))
        notaminimamat = questoesmat * porcentminimamat
        notaminimaport = questoesport * porcentminimaport
        if (notadeportugues >= notaminimaport):
            if (notadematematica >= notaminimamat):
                if (notaderedacao >= notaminimared):
                    qtdaprovados += 1

print (qtdaprovados)
