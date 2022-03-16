dist = float(input('Distância em Km: '))
if dist > 200:
    print('Valor total: R${}'.format(dist * 0.45))
else:
    print('Valor total: R${}'.format(dist * 0.50))