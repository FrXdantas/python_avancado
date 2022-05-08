
total = 0

for i in range(0,500):
    resto = i%2
    if resto != 0:
        total += i
        
print(f'a soma dos numeros pares entre 0 e 500 é: {total:2} ')