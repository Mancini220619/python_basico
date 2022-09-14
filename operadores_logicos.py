"""
and - e
or - ou
not - inversor
in - tem no texto ou int
not in - inverso de 'in'
"""


nome = input('nome: ')
idade = int(input('qual idade: '))
idademin = 18
idademax = 30

#verdadeiro e verdadeiro

#quando usar 'or' só precisa satisfazer uma condição

if idade >= idademin and idade <= idademax:
    print (f'conceder emprestimo a {nome}')
else:
    print (f'nao conceder emprestimo a {nome}')




a=2
b=2
c=3

print(a==b and b < c)
print(a==b or b < c)


# uso do not

a=2
b=3

if not b > a:
    print ('b maior q a')
else:
    print ('a maior q b')

a = ''
b = 0 #0 zero é considerado um valor falso em booleano

if not a:
    print('preencha valor de a')


#usando in
nome = "Juliano"

if 'Ju' in nome:
    print ('tem a letra Ju no nome')
else:
    print('nao existe o texto')