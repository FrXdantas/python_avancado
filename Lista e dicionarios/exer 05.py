perguntas= {
            '1':'A) Telefonou para a  vitima? ',
            '2':'B) Esteve no Local do Crime? ',
            '3':'C) Mora perto da vitíma? ',
            '4':'D) Devia algo para vítima? ',
            '5':'E) Já trabalhou para a vitima? '
            }

rspt=[]


for i in range(1,6):
    p = str(i)
    rs=(input(perguntas.get(p)))
    rspt.append(rs.lower())
 
analise = rspt.count('sim')

if analise ==5:
    print('\nAnalise : Possivel assassino ')
elif analise ==4 or analise ==3:
    print('\nAnalise : Possivel cumplice ')
elif analise == 2:
    print ('\nAnalise : Possivel Suspeito ')
else:
    print('\nAnalise : Inocente, pode liberar')
    



