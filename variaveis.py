"""
iniciar com letras, pode conter numeros, separar _, letras minusculas
"""

nome = 'Juliano'
idade = 37
altura = 1.80
e_maior = idade > 20
peso = 98

print('Meu nome é:', nome)
print('Minha idade é:', idade)
print('Altura é:', altura)
print('Sou maior de 20:', e_maior)

print (nome, 'tem', idade, 'anos de idade e seu imc é', peso/(altura**2))