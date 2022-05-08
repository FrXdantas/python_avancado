import random

mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
temperatura=[]

for i in range(12):
    temperatura.append(random.randint(-2, 44))
temm=round(sum(temperatura)/len(temperatura))


for i in range(12):
    print(f'{mes[i]:12} - {temperatura[i]:2}º')
    
print (f'\nA temperatura média foi de {temm}º.\n')

for y in range(12):
    if temperatura[y]>temm:
        print(f'{mes[y]:12} - {temperatura[y]:2}º')
