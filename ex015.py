d = int(input('Quantos dias alugado? '))
k = float(input('quantos Km rodados? '))
p = (60*d) + ( 0.15*k)
print('O total do aluguel é de R$ {:.2f}'.format(p))

