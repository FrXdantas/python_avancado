#importa a biblioteca randomica, usei para gerar idade e alturas aleatórias.
import random

qtd = int(input("Qual tamanho da lista: "))

indx = []
idade = []
altura= []

#geração de idades e alturas diversas e aleatórias.

for x in range(0,qtd):
        indx.append(x)
        #idade entre 10 e 16
        idade.append(random.randint(10,16))
        #altura entre 1 mt e 1.60
        y= random.uniform(1.0,1.60)
        #convertendo a altura em 2 casas decimais
        altura.append(round((y),2))

for i in range(qtd):
    print(f'{i+1:2}-{idade[i]:3} - {altura[i]:2}')


media = (sum(altura)/len(altura))        
      
total=0
print("Media de Altura é {:.2f} ".format(media))  

print("Alunos Abaixo da altura média: \n")
for y in range(qtd):
    if idade[y] > 13 and altura[y]<media:
        print(f'{indx[y]+1} - {idade[y]:3} - {altura[y]:2}')
        total+=1

print ('\nTotal de Alunos com mais de 13 anos abaixo da média de altura {} '.format(total))        