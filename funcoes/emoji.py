def emojis (mensagem):
    palavras = mensagem.split(" ")
    #Transforma a partir de um dicionario, caracteres em emoji
    emoji={
        ":)": "😊",
        ":(": "🙁",
        "LMFAO": "🤣"

    }

    output = ""
    for x in palavras:
        output += emoji.get(x, x) + " "
    return output


