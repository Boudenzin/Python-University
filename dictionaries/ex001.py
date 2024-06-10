# Programa que converte número inteiro pelo seu referencial em extenso

numbers = {
    "1": "Um",
    "2": "Dois",
    "3": "Três",
    "4": "Quatro",
    "5": "Cinco",
    "6": "Seis",
    "7": "Sete",
    "8": "Oito",
    "9": "Nove",
    "0": "Zero",
}



phone = str(input("Phone: "))

output = ""
for x in phone:
    output += numbers.get(x, "!") + " "
print (output)


