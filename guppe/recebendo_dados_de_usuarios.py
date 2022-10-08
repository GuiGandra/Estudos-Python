"""
Recebendo dados do usuario

input()-> todo dado recebido via input é uma string

Em Python strin é tudo que estiver entre:
- Aspas simples;
- Aspas duplas ;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Gandra'
- Aspas duplas -> "Gandra"
- Aspas simples triplas -> '''Gadra'''
"""
# - Aspas duplas triplas -> """Gandra"""


# Entrada de dados
#print("Qual seu nome?")
#nome = input() # input -> Entrada

nome = input('Qual seu nome ?')

# Exemplo antigo de print 'antigo' 2.x
# print('Seja bem vindo(a) %s' % nome)

#Exemplo de print 'Moderno' 3.x
# print('Seja bem vindo(a) {0}'.format(nome))

#Exemplo de print 'mais atual' 3.7x

print(f'Seja bem-vindo(a) {nome}')

#print("Qual sua idade?")
#idade = input()

idade = int(input('Qual sua idade ?'))

# Processamento

# Saida de dados
# Exemplo de print 'antigo' 2.x
# print('O(A) %s tem %s anos' % (nome, idade))

#Exempo de print 'Moderno' 3.x
# print('O(a) {0} tem {1}'.format(nome,idade))

#Exemplo de print 'mais atual' 3.7

print(f'O(a) {nome} tem {idade} anos')
"""
int(idade) ->cast

Cast é a 'conversão' de um tipo de dado para outro
"""
print(f'O(a) {nome} nasceu em {2021 - idade}')

input('Quanto é 2+2?')
