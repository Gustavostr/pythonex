import math
ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))
hi = pow(ca, 2) + pow(co, 2)
ra = math.sqrt(hi)
print('A hipotenusa é {:.2f}'.format(ra))

