'''
While

Utilizado para realizar ações enquanto uma instrução for verdadeira

'''
'''
x = 0
while x < 5:
    print(x)
    x = x + 1
print('acabou!')

print(5<5)


x = 0
while x < 10:
    if x == 3:
        print('chegou em 3', x)
        #x += x
        x += x
        #continue #pula para o proximo laço
        break # com break ele finaliza o bloco de codigo e pula pro final
    print(x)
    x = x + 1
print('acabou!')

'''


x = 0

while x < 10:
    y = 0
    
    while y < 5:
        
        y+=1
        print (f'{x},{y}')

    x += 1 # x = x + 1


print ('acabou')