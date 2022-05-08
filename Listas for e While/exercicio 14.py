valor = 0
total = 0


while valor < 501:
    
    cont = valor%2
    
    if cont != 0:
       
        total += valor
        print(valor, total)
    valor = valor + 1
      
    
print('total da soma dos impares {} : '.format(total))

