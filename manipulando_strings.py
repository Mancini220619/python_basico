'''
Manipulando strings

string - indices
fatiamento de strings [inicio:fim:passo]
funções built-in len, abs, type, print, etc...
essas funções podem ser usadas diretamente em cada tipo

https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/stdtypes.html
'''

#positivos  [012345678]
texto   =   'Sistema_()'
#negativos -[987654321]

print (texto[8])
print (texto[4])
print (texto[4:8])

url = 'www.google.com.br/'
print (url[:-1]) #:-1 imprime sem o ultimo caracter '/'

nova_string = texto[3:6]
print (nova_string)

a = texto[0::2]
b = texto[0:8:3]
print(a)
print(b)

print (len(texto))
print()

print(texto)
texto_1 = 'caiu'
for letra in texto_1:
    print(letra)
