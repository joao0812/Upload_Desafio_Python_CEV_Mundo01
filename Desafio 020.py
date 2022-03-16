from random import shuffle
from os import remove
# x = 0
# aux = ''
# ordem = []

aluno01 = input('Aluno 01: ')
aluno02 = input('Aluno 02: ')
aluno03= input('Aluno 03: ')
aluno04 = input('Aluno 04: ')

lista = [aluno01, aluno02, aluno03, aluno04]
print(lista)
shuffle(lista)
print(lista)

# while x != 4:
#    if x != 0:
#        while esc in ordem:
#            esc = random.choice(lista)
#        ordem.append(esc)

#    if x == 0:
#        esc = random.choice(lista)
#        ordem.append(esc)
#    print(ordem)
#    x = x + 1
