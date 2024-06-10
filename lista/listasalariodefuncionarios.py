"""setores_empresa = []
salario_funcionarios = []
quant_funcionarios = 3
setores_contemplados = []
aumento = 1.2
gasto_extra = 0

for i in range (1, quant_funcionarios + 1):
    setor = str.title(str.lower(input(f"Qual o setor do funcionário {i}: ")))
    salario = float(input(f"Qual o salário do funcionário {i + 1}: "))
    setores_empresa.append(setor)
    salario_funcionarios.append(salario)

for i in range (quant_funcionarios):
    if (setores_empresa[i] == "Recursos Humanos") or (setores_empresa[i] == "Almoxarifado"):
        aumento_salario = salario_funcionarios[i] * aumento
        setores_contemplados.append(aumento_salario)
        gasto_extra += (aumento_salario - salario_funcionarios[i]) 

if (gasto_extra != 0):
    print (f"Gasto Extra da Empresa: {gasto_extra}")
    print (f"Salário Aumentados: {setores_contemplados}")
else:
    print (f"Nenhum setor foi promovido")
"""


setores_contemplados = []
gasto_extra_empresa = 0

quant_funcionarios = 3
porcentagem_aumento = 1.2

dados_funcionarios = []
for i in range(1, quant_funcionarios + 1):
    dados_funcionario = {
        "Setor": str.title(str.lower(input(f"Qual o setor do funcionário {i}: "))),
        "Salário": float(input(f"Qual o salário do funcionário {i}: "))
    }
    dados_funcionarios.append(dados_funcionario)

for funcionario in dados_funcionarios:
    setor = funcionario["Setor"]
    salario = funcionario["Salário"]

    if setor in ["Recursos Humanos", "Almoxarifado"]:
        aumento_salarial = round(salario * porcentagem_aumento, 2)
        setores_contemplados.append({"Setor": setor, "Aumento": aumento_salarial})
        gasto_extra_empresa += aumento_salarial - salario

if setores_contemplados:
    print(f"Gasto Extra da Empresa: R${gasto_extra_empresa:.2f}")
    print(f"Salários Aumentados: {setores_contemplados}")
else:
    print("Nenhum setor foi contemplado com aumento salarial.")

