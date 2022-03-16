cpf = input('Digite seu CPF: ')
print(cpf)

cpf = list(cpf)
cpf.append(' ')
cpf.append(' ')
cpf.append(' ')
print(cpf)

for i in range(len(cpf)-1, 2, -1):
    cpf[i] = cpf[i-1]
cpf[3] = '.'
print(cpf)

for i in range(len(cpf)-1, 6, -1):
    cpf[i] = cpf[i-1]
cpf[7] = '.'
print(cpf)

for i in range(len(cpf)-1, 8, -1):
    cpf[i] = cpf[i-1]
cpf[11] = '-'
print(cpf)
# for i in range(0, len(cpf)-1, +3):
#    print(cpf[i])
