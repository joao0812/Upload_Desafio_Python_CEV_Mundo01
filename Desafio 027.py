nome = input('Digite seu nome: ')

nome = nome.split()
cont = len(nome)
print('Primeiro nome: {}\nÚltimo nome: {}'.format(nome[0].capitalize(), nome[cont-1].capitalize()))
