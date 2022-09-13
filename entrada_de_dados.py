"""
entrada de dados

função input sempre retorna uma string

"""

nome = input('qual seu nome? ')
idade = input ('qual sua idade? ')

#dessa forma dá erro >>>> anonasc = 2022 - idade >>>> pois estamos subtraindo um inteiro de uma string

anonasc = 2022 - int(idade)

print(f'Meu nome é: {nome}, tenho {idade} anos de idade e nasci no ano de {anonasc}')


##########################################################

num1 = (int (input ('digite 1 num: ')))
num2 = int (input ('digite 2 num: '))

print (num1+num2)