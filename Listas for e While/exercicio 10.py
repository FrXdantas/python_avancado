n1 = int(input('digite um numero: '))
c = 0

for i in range(2, n1+1):
    if n1 % i == 0:
        c = c+1
if c <= 2:
    print('O numero {} é divisivel {} vezes,  é um numero primo'.format(n1, c+1))
else:
    print('O numero {} é divisivel {} vezes, ele não é um numero primo'.format(n1,c))   