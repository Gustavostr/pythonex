pessoa = str(input("Digite o nome de uma pessoa: "))
pessoa = pessoa.upper()
c = 'SILVA' in pessoa

if c:
    print("essa pessoa tem Silva")
else:
    print("essa pessoa não tem silva")
