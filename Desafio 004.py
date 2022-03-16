n1 = input('Digite Algo ')

print(type(n1))
# print(n1.isnumeric())
# print(n1.isalpha())
# print(n1.isalnum())

if n1.isalpha():
    print('Você digitou apenas letras')

if n1.isnumeric():
    print('Você digitou apenas números')

if n1.isalpha() == False and n1.isnumeric() == False:
    # if n1.isnumeric() == False:
    print('Você digitou letras e números')