cidade = input('Digite o nome da sua ciadade: ')
cidade = cidade.split()
print(cidade)
if cidade[0].upper().find('SANTO') == -1:
    print('A cidade não começa com Santo')
else:
    print('A cidade começa com Santo')
