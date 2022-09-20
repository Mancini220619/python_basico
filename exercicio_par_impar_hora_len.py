###############################primeiro exercicio

num1 = input('digite um numero: ')

if num1.isdigit():
    num1= int (num1)
    num = num1 % 2
    print(f'resto da divisão é {num}')   #se resto da divisao for 0 é par

    if (num1 % 2) == 0:
        print(f'{num1} é um numero par')
    else:
        print(f'{num1} é um numero impar')
else:
    print ('error')



###############################segundo exercicio
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

hora = input ('digite a hora: ')

if is_int (hora):
    a = int(hora)
    if a >= 0 and a <= 11:
        print ('bom dia')
    elif a >= 12 and a <= 17:
        print ('boa tarde')
    else:
        print ('boa noite')
else:
    print('digite um numero inteiro')

###############################terceiro exercicio

nome = input ('digite seu nome: ')
qtd = len (nome)

if qtd <= 4:
    print ('seu nome é curto')
elif qtd >=5 and qtd <= 6:
    print('nome é normal')
else:
    print ('seu nome é longo')
