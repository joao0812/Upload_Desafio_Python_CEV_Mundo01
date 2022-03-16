salario = float(input('Digite o valor do salário: '))

if salario > 1250:
    print('Reajustado para: R${:.2f}'.format(salario*1.1))
else:
    print('Reajustado para: R${:.2f}'.format(salario*1.15))