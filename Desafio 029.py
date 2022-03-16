import colorama
velocidade = int(input('Digite a velocidade do carro em Km/h: '))

if velocidade >= 80:
    print(colorama.Fore.RED + 'MULTADO! valor da Multa: R${:.2f}'.format((velocidade-80)*7))
else:
    print('Tudo certo, siga em frente!')