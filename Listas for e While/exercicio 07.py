print('Os numeros pares entre 1 e 50 são: ')
for i in range(1,51):
    resto = i%2
    if resto != 1:
        print(f'{i:2}')
