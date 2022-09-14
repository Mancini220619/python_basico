"""
operadores relacionais 
== igualdade
> maior
>= maior ou igual
< menor
<= menor ou igual
!= diferente
"""

num1 = 2
num2 = 1
print (num1 >= num2)

nome = input ('qual seu nome? ')
idade = int (input ("qual sua idade? "))
libera = 18

print (type(libera))

if (idade >= libera):
    print('{} pode pegar o emprestimo'.format (nome))
else:
    print('{} emprestimo negado, menor de idade'.format (nome))

print()
#####################################################


nome = 'Joãozinho'
idade = """40"""
peso = 80.5
e_maior = True
idade = int(idade)
 
if idade > 18:
    print(f'{nome} é maior de idade.')
else:
    print(f'{nome} NÃO é maior de idade.')