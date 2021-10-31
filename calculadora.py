operation = input('''
Qual operação você quer fazer? Insira um dos operadores:
+ para adição
- para subtração
* para multiplição
/ para divisão
''')

number_1 = int(input('Insira um número: '))
number_2 = int(input('Insira o segundo número: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('você incluiu o operador errado, corrija o erro e tente novamente.')
    

#Continuação dos estudos:
#Incluir operações infinitas com funções
#site: https://www.digitalocean.com/community/tutorials/como-fazer-um-programa-de-calculadora-simples-no-python-3-pt
