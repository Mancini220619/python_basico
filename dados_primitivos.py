"""
tipos de dados
str-string - textos "assim" ou 'assim'
int - inteiro - 123456, 10 ,0 -11, 06 78
float - flutuante - 0.1 , 10.50, -8.76
bool - booleano/logico - true/false 10==10
"""

print('Juliano', type('Juliano'))
print(10, type (10))
print(91.10, type (91.10))
print(10==10, type(10==10))

#transformar string em bool, quando bool geralmente esta vazio, zero 0 é false

print('Juliano', type('Juliano'), bool('Juliano'),bool(''))

#converter str em inteiro

print('10', type('10'), type(int('10')))

print('10', type ('10'), type(float('10')), float('20'))

print(10+10)

print('10'+'10') # junta 10 com 10 resultado 1010





#string: nome
print('Juliano Mancini', type('Juliano Mancini'))

#idade: int
print(10, type(10))

#altura: float
print(1.89, type(1.89))

#é maior 32 > 18
print(32 > 18, type(32 > 18))

