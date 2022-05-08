valor = int(input('Digite um valor : '))
n=0
qtd=0


while n*n < valor:
    
    qtd = n*n
   
    print('Quadrados :',qtd)
    
    n = n + 1
    
while n < valor:
    
    qtd = n%10
   
    if qtd==0 :
        
        print('Divisiveis por 10: ',n)
    n = n+1
    
n = 0

while qtd < valor:
    
    qtd = 2 ** n
    
    if qtd < valor:
        
        print ('O valor é : ',qtd)
    
    n=n+1
  
