totalapagar = 0
totalconvidados = 0
senhamaxporpessoa = 15
senhaextramaxporpessoa = 10
precosenhaextra = 42
resposta = "SIM"
while (resposta == "SIM"):
    pgtsenhaextra = 0
    convidadosextras = 0
    convidados = int(input("Qts convidados? "))
    if(convidados > senhamaxporpessoa):
        if (convidados > senhaextramaxporpessoa):
            convidadosextras = senhaextramaxporpessoa
        else:
            convidadosextras = convidados - senhamaxporpessoa
        pgtsenhaextra = precosenhaextra * convidadosextras
    totalapagar += pgtsenhaextra
    totalconvidados += convidados
    resposta = str.upper(input("Quer adicionar mais convidados? (SIM/NÃO)"))
print (totalapagar)
print (totalconvidados)
