total_gasto = 0
total_acima = 0
carrinho = []
while True:
    try:
        produtos = str(input("Digite o nome do produto: "))
        custo = float(input("Digite o preço do produto: "))
        total_gasto += custo 
        if custo > 1000:
            total_acima += 1
        carrinho.append((custo,produtos))
        carrinho.sort()
    except ValueError:
        print("inválido")
    while True:
        condicao = str(input("Quer continuar [S/N]?").upper())
        if condicao == "S" or condicao == "N":
            break
    if condicao == "N":
        break
print("="*45)
print(f"O total da compra foi {total_gasto} reais!")
print(f"Foram {total_acima} acima de mil reais!")
print(f"O produto mais barato é {carrinho[0][1]} é custa R${carrinho[0][0]}!")



