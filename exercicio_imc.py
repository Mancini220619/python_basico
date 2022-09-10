"""
criar variaveis para nome (str), idade (int)
altura (float) e peso (flot) de uma pessoa
criar variavel com o ano atual (int)
obter o ano de nascimento da pessoa basedo na idade e no ano atual
obter imc da pessoa com 2 cas decimais (peso e na altura da pessoa)
exibir um texto com todos os valores na tela usando F-strings (com chaves)
"""
import datetime
x = datetime.datetime.now()
x = int (x.strftime("%Y"))

nome = str('Juliano')
idade = int(37)
altura = float(1.89)
peso = float (98.5)
ano = int(2022)
datanasc = x - idade
imc = peso / altura **2

print ('Meu nome é {n}, minha idade é {i}, altura {a} e meu peso {p}'.format(n=nome,i=idade,a=altura,p=peso))
print ('Nascido no ano de {}'.format (datanasc))
print ('Meu imc é {:.2f}'.format(imc))