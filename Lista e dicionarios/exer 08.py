qtd =int(input('Quantas pessoas deseja cadastrar ?: '))

todos={}
menores={}

nome  = []
idade = []
cpf   = []

nomem  = []
idadem = []
cpfm   = []


todos['nome'] =nome
todos['idade']=idade
todos['cpf']=cpf

menores['nome'] =nomem
menores['idade']=idadem
menores['cpf']=cpfm



for i in range(0,qtd):
    n1 = input('Digite o Nome:  ')
    n2 = int(input('Digite a Idade: '))
    n3 = input('Digite o CPF  : ')
    
    nome.append(n1.lower())
    idade.append(int(n2))
    cpf.append(str(n3))
    
    
    
    if n2<18:
      
        nomem.append(n1.lower())
        idadem.append(int(n2))
        cpfm.append(str(n3))

for chave,valor in todos.items():
    print(f'{chave:10} - {valor}')

print (' : Menores de Idade : ')
for chave,valor in menores.items():
    print(f'{chave:10} - {valor}')
    






    
