frase =  input('Escreva um frase: ')

print('Quantidade de letras A: {}\nComeçando na posição: {}\nTerminando na posição:'.format(frase.upper().count('A'), frase.upper().find('A') + 1), frase.upper().rfind('A') + 1)