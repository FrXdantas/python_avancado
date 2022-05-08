A = []
Aq= []

p = int(input('digite um valor para gerar lista: '))

for i in range (p):
    A.append(i+1)



for x in A:
   qdd=x*x
   Aq.append(qdd)

for y in range(p):
    print (f'{A[y]} - {Aq[y]}')

print(f'A Soma dos quadrados : {sum(Aq)}')
