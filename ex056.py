lista = []
veto = []

for p in range(1,5,1):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo: "))
    pessoa = (nome, idade, sexo)
    if sexo == "masculino":
        lista.append(pessoa)
    else:
        veto.append(pessoa)

pessoa_com_maior_idade = max(lista, key=lambda pessoa: pessoa[1])
mulher = max(veto, key=lambda pessoa: pessoa[1])

print(f"A pessoa com a maior idade é {pessoa_com_maior_idade[0]} com {pessoa_com_maior_idade[1]} anos.")
soma_idades = sum(pessoa[1] for pessoa in lista)
soma = sum(pessoa[1] for pessoa in veto)
media_idades = (soma_idades + soma ) / (len(lista) + len(veto))
print(f"A média das idades é {media_idades}.")
print("A mulher com maior idade é: {}".format(mulher))

