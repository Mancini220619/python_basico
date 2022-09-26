'''
formatando valores com modificações

:s - texto (string)
:d - inteiros
:f - numeros de ponto flutuante (float)
:.(numero) f - quantidade de casas decimais (float)
:(caractere) (> ou < ou ^) (quantidade)(tipo -s, d ou f)

> - esquerda
< - direita
^ - centro
'''

num_1 = 10
num_2 = 3

divisao = num_1 / num_2
print('{:.2f}'.format (divisao))
print(f'{divisao:.3f}')

nome = 'juliano'
print(f'{nome:.2s}')

num1 = 1
num2 = 123
print(f'{num1:0>10}') # a esquerda preencher com 9 zeros + num1
print(f'{num2:0<10}') # a direita num2 + quantidade de zeros ate 10

print(f'{num2:.2f}')

print(f'{num2:0>10.2f}')

nome = 'juliano'
meio = 'carlos'
sobre = 'mancini'

print('{n:$^50} {m:!^50} {s:#^50}'.format(n=nome,m=meio,s=sobre))
print('{0:$^50} {1:#^50}'.format(nome,sobre))

nome = 'Juliano CarloS ManCini'

print(nome.lower())
print(nome.upper())
print(nome.title())
