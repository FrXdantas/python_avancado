
#lista 3
#Exercicio 01

def calcular_media(n1,n2,n3,n4):
    
    n1 =float(input('Nota da Lista  1 - 0 até 2  : '))
    
    n2 =float(input ('Nota da Lista 2 - 0 até 2  : '))
    
    n3 =float(input('Nota da Lista  3 - 0 até 2  : '))
    
    n4 =float(input('Nota do Mini projeto 0 - até 4:'))
    
    return(n1+n2+n3+n4)

media2=float(calcular_media(0,0,0,0))


print(f'A Média do Aluno foi {media2:.2f}')

    