km_corrido = float(input('Quantos Km seu veículo percorreu? '))
dias_alugados = int(input('O veículo foi alugado por quntos dias? '))

total_carro = (km_corrido*0.15) + (dias_alugados*60)

print('TOTAL: R${:.2f}'.format(total_carro))