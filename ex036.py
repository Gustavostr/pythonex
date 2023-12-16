valor_casa = float(input("Digite o valor da casa que você quer comprar: "))
salario_comprador = float(input("Digite o seu salário mensal: "))
anos_divida = float(input("Digite quantos anos você quer quitar a casa: "))
prestacao_mensal = float( valor_casa / (anos_divida*12))
if  prestacao_mensal > (30/100 * salario_comprador):
    print ("suas parcelas exedem 30% do seu salário, portanto seu empréstimo foi negado")
else:
    print ("Parabéns seu empréstimo foi concedido com sucesso!!! \n suas parcelas são {:.2f}R$ por mês".format(prestacao_mensal))
