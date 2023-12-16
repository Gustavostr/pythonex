print("Digite a forma de pagamento: \n 1 - À vista no dinheiro/cheque! \n 2 - À vista no cartão! \n 3 - até 2x no cartão \n 4 - 3x ou mias no cartão ")
preco = float(input("Digite o valor da compra: "))
paga = int (input("Selecione a forma de pagamento: "))
if paga == 1:
    print("Total a pagar R${} reais".format(preco - 10/100*preco))
elif paga == 2:
    print("Total a pagar R${} reais".format(preco - 5/100*preco))
elif paga == 3:
    parc = int(2)
    print("Total a pagar R${} reais em parcelas de {}".format(preco, preco/parc))
elif paga == 4:
    tot = preco + 20/100*preco
    parc = int(input("Digite quantas parcelas você quer pagar: "))
    print("Total a pagar R$ {} reais em parcelas de {:.2f}".format(tot, tot/parc))
else:
    print ("forma inválida")
