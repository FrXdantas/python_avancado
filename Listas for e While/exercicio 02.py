vendas = []
valor  =[]
sair ='n'

while sair != 's':
    
    x = (str(input('Digite o produto para venda: ')))
    y = (int(input('Digite o valor do produto  : ')))
    
    vendas.append(x)
    valor.append (y)
    
    sair = (input('Deseja encerrar a venda : (s) para sair: '))
    
for i in range (len(vendas)):
    print(f'{vendas[i]} - R$ {valor[i]}')
print(f'Total da compra foi de : {sum(valor)}')