import math

co = float(input('Valor do Cateto oposto: '))
ca = float(input('Valor do Cateto adjacente: '))

hip = math.sqrt((co**2) + (ca**2))

print('O valor da Hipotenusa vale: {:.2f}'.format(hip))
