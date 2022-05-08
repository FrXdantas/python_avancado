print('Os numeros pares entre 1 e 50 sÃ£o: ')
n=[]
total = 0
for i in range(0,6):
    n.append(int(input('Digite um numero inteiro: ')))

print('\nA soma dos pares é :\n')

for i in n:
    resto = i%2
    if resto != 1:
        total+= i
        print(f'{i:2}')
print(f'\n=====\n{total:2}')
