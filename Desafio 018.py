import math
ang = float(input('Digite o valor do ângulo: '))

cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tag = math.tan(math.radians(ang))

print('Para o ângulo {:.2f}\nCOSSENO: {:.2f}\nSENO: {:.2f} \nTANGENTE: {:.2f}'.format(ang, cos, sen, tag))


