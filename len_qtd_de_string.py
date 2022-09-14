"""
contar string
"""




nome1 = input ('digite 1 nome: ')
nome2 = input ('digite 2 nome: ')

print(f'a qtd de caracteres totais é de: {len(nome1) + len(nome2)}')

print(nome2.__len__())


usuario = input ('digite seu usuario: ')
qtd_caract = len(usuario)

print (usuario, qtd_caract, type (qtd_caract))
