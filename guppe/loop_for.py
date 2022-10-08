"""
Loop for

Loop -> Estrutura de repetição
For-> Uma das estruturas de repetição

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequencias ou sobre valores interaveis
-String
    nome = 'Guilherme'
-Lista
    lista = [1, 3, 5, 7, 9]
-Range
    numeros = range(1, 10)

range(valor_inicial, valor_final)

# Exemplo de for 1 (Iterando em uma string)

for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

for numero in range(1, 10):
    print(numero)


OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não

Enumerate:

((0, 'G'), (1, 'u'), (2, 'i'), (3, 'l'), (4, 'h'), (5, 'e'), (6, 'r'), (7, 'm'), (8, 'e'))

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartalo utilizando um (_)

nome = 'Guilherme'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse dado deve rodar?'))

for n in range(1, qtd+1):
    print(f'Imprimindo{n}')

qtd = int(input('Quantas vezes esse dado deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'soma é {soma}')

nome = 'Guilherme'
for letra in nome:
    print(letra, end='')

(end='')- cancela o comando do print que sempre imprime na proxima linha

Tabelas de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""


#Original :U+1F60D
#Modificado: U0001F60D


for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)

