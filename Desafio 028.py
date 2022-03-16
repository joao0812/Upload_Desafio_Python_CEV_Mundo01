import random
resultado = False
valor = random.randint(0, 5)
vida = 1

while resultado == False:
    n1 = int(input('Qual número eu estou pensando entre 0 e 5: '))

    if n1 == valor:
        print('Parabéns você acertou! ')
        resultado = True
    else:
        print('Não foi esse, vamos tente novamente!')
        print('Chances: {}/3'.format(vida))
        vida = vida + 1
        if vida == 4:
            print('FIM DE JOGO!')
            resultado = True

