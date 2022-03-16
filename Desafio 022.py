nome = input('Digite seu Nome: ')
nome = nome.strip()

print(nome.upper())

print(nome.lower())

espaco = int(nome.count(' '))
quant_nome = len(nome)
total = quant_nome - espaco
print(total)

nome = nome.split()
print(len(nome[0]))

