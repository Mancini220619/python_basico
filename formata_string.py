nome = 'Juliano'
idade = 37
altura = 1.89
e_maior = idade > 20
peso = 98
imc = peso / (altura**2)

print('Meu nome é:', nome)
print('Minha idade é:', idade)
print('Altura é:', altura)
print('Sou maior de 20:', e_maior)

print (nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print (f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}') #2.f exibe 2 duas casas

print ('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome,idade,imc))

print ('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome,idade,imc))

print ('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome,i=idade,im=imc))