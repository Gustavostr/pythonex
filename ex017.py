import math
#ca = float(input('Digite o cateto adjacente: '))
#co = float(input('Digite o cateto oposto: '))
#hi = pow(ca, 2) + pow(co, 2)
#ra = math.sqrt(hi)
#print('A hipotenusa é {:.2f}'.format(ra))

# Depois de estudar algumas funcionalidades do módulo, achei essa outra forma mais eficiente



ca = float(input('Digite o cateto: '))
co = float(input('Digite o outro cateto: '))
r = math.hypot(ca, co)
print('A hipotenusa é {:.2f}'.format(r))



