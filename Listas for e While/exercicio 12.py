cont = 0
lista=[]

while cont < 5:
    
    num = int(input('digite um numero: '))
    lista.append(int(num))
    cont = cont+1
    
    
print (f'Maior numero digitado foi {max(lista)}')
print (f'Maior numero digitado foi {min(lista)}')       