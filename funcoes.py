'''
PYTHON é de tipagem dinamica

ele nao vai converter um tipo em outro

>>>>funções isnumeric isdigit isdecimal - somente numeros positivos e inteiros<<<<

ou podemos usar 
try:
except:

a = input ('digite: ')
b = input ('digite: ')

try:
    a = float(a)
    b = float(b)

    print(a+b)
except:
    print('ERROR')
'''

import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)


a = input ('digite: ')
b = input ('digite: ')

if is_number (a) and is_number (b):
    a = float (a)
    b = float (b)
    print(a+b)
else:
    print('ERROR')
