def defineEstacao(mes):
    primavera = ["setembro", "outubro", "novembro"]
    verao = ["dezembro", "janeiro", "fevereiro"]
    outono = ["março", "abril", "maio"]
    inverno = ["junho", "julho", "agosto"]

    if (mes.lower() in primavera):
        return "Primavera"
    if (mes.lower() in verao):
        return "Verão"
    if (mes.lower() in outono):
        return "Outono"
    if (mes.lower() in inverno):
        return "Inverno"
    

