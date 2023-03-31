import math
angulo = int(input("Digite um ângulo para saber o sen, cos e tg: "))
rad = math.radians(angulo)
seno = math.sin(rad)
cos = math.cos(rad)
tag = math.tan(rad)
print(' O seno de {} é {:.2f}'.format(angulo, seno))
print('O cosseno de {} é {:.2f}'.format(angulo, cos))
print('A tangente de {} é {:.2f}'.format(angulo, tag))



# a forma mais otimizada para isso seria
# seno = math.sin(math.radians(angulo))
# sendo assim, dispensável a variável rad criada e otimizando o código

