import random
aux = ' '
aluno01 = input('Aluno 01: ')
aluno02 = input('Aluno 02: ')
aluno03= input('Aluno 03: ')
aluno04 = input('Aluno 04: ')

lista = [aluno01, aluno02, aluno03, aluno04]
while aux == ' ':
    print(random.choice(lista))
    aux = input('')