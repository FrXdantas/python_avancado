import os

#funções diversas

def tela():
    print("#" * 71)
    print("#" * 20, "SISTEMA DE REAJUSTE", "#" * 30)
    print("#" * 71)


def limpar():
    os.system('cls')
    os.system('color 1E')


def pausar():
    os.system('pause')


limpar()
tela()
print("\nAJUSTE OS PAREMETROS DO SISTEMA :\n")

qtd = int(input("Digite a quantidade de fucionários    : "))
sma = float(input("Digite o valor atual do salário minimo: "))
print("\n")
folha = 0
nvfolha = 0
reajuste = 0

func = []
slant = []
reaj = []
novosal = []
por = []

limpar()
tela()

# mostra na tela o valor do salário atual

print("\nLANÇAMENTOS DO SISTEMA       VALOR DO SALARIO ATUALMENTE      R$ {}\n".format(sma))

x: int

# entrada de dados dos funcinários

for x in range(0, qtd):
    print("\n{}º - Lançamento".format(x + 1))
    nome = str(input('Digite o nome do funcionario : '))
    func.append(nome)
    sal = float(input('Digite o salário atual       : '))
    slant.append(sal)

#desvios e calculos

    if sal <= sma * 3:
        reajuste = (sal * 50 / 100)
        reaj.append(reajuste)
        nvsal = (reajuste + sal)
        novosal.append(nvsal)
        por.append("50%")
        folha = (folha + sal)
        nvfolha = (folha + reajuste)

    elif sal >= sma * 3 and sal <= sma * 10:
        reajuste = (sal * 20 / 100)
        reaj.append(reajuste)
        nvsal = (reajuste + sal)
        novosal.append(nvsal)
        por.append("20%")
        folha = (folha + sal)
        nvfolha = (folha + reajuste)

    elif sal >= sma * 10 and sal <= sma * 20:
        reajuste = (sal * 15 / 100)
        reaj.append(reajuste)
        nvsal = (reajuste + sal)
        novosal.append(nvsal)
        por.append("15%")
        folha = (folha + sal)
        nvfolha = (folha + reajuste)

    elif sal > sma * 20:
        reajuste = (sal * 10 / 100)
        reaj.append(reajuste)
        nvsal = (reajuste + sal)
        novosal.append(nvsal)
        por.append("10%")
        folha = (folha + sal)
        nvfolha = (folha + reajuste)

limpar()
tela()


# cabeçalho da tela final

print("\nLANÇAMENTOS DO SISTEMA       VALOR DO SALARIO ATUALMENTE      R$ {}\n".format(sma))
print("\nNº  FUNCIONARIO             SALARIO  PORC          REAJUSTE  VLOR FINAL")
print("=======================================================================\n")

#lista de funcionários e reajustes
for x in range(0, qtd):

    print(f'{x+1} - {func[x]:17} {slant[x]:13.2f}  {por[x]:5} {reaj[x]:15.2f} {novosal[x]:12.2f}')


#formatação de saida

cfolha=folha
folha = f'R$ {folha:_.2f}'
folha = folha.replace('.',',').replace('_','.')
vlReajust = (sum(reaj))
vlReajust = f'R$ {vlReajust:_.2f}'
vlReajust = vlReajust.replace('.',',').replace('_','.')
vlFinal = (cfolha+sum(reaj))
vlFinal = f'R$ {vlFinal:_.2f}'
vlFinal = vlFinal.replace('.',',').replace('_','.')

#Saida depois de processado e formatado

print("\nRESUMO DE IMPACTO NA FOLHA DE PAGAMENTO ")
print("=======================================================================\n")
print(f"Valor da folha de pagamento.....: {folha}")
print(f"Valor de Reajuste...............: {vlReajust}")
print(f"Valor da nova Folha de Pagamento: {vlFinal}\n")
print("=======================================================================\n\n")

with open('nova_folha.txt','w') as arquivo:
   arquivo.write("RESUMO EM TXT DOS LANÇAMENTOS\n\n")
   arquivo.write ("Nº  FUNCIONARIO             SALARIO  PORC          REAJUSTE  VLOR FINAL\n")
   arquivo.write("=======================================================================\n\n")
   for x in range(0,qtd):
       arquivo.write(str((f'{x+1} - {func[x]:17} {slant[x]:13.2f}  {por[x]:5} {reaj[x]:15.2f} {novosal[x]:12.2f}'))+'\n')

   arquivo.write("\nRESUMO DE IMPACTO NA FOLHA DE PAGAMENTO "+"\n\n")
   arquivo.write("=======================================================================\n\n")
   arquivo.write(f"Valor da folha de pagamento.....: {folha}"+"\n")
   arquivo.write(f"Valor de Reajuste...............: {vlReajust}"+"\n")
   arquivo.write(f"Valor da nova Folha de Pagamento: {vlFinal}\n"+"\n")
   arquivo.write("=======================================================================\n")


pausar()