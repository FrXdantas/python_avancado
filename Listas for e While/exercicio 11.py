lista=[]

for i in range(1,7):
    lista.append(int(input('Digite a idade: ')))

maior = 0
menor = 0

for i in lista:
    if i >= 18:
        maior += 1
    else:
        menor += 1

print('maiores de idade {}'.format(maior))
print('menores de idade {}'.format(menor))