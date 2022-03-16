altura = float(input('Digite a altura da sua parede: '))
largura = float(input('Digite a Largura da sua parede: '))

area = altura * largura

print('Para uma parede com {:.2f}m² serão necessários {}L de tinta'.format(area, round(area/2 + 0.5)))