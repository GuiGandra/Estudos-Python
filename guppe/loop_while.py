"""
Loop While

Forma geral

while expressão_booleana:
    //execução do loop

O bloco do while sera repetido em quanto a expressão booleana for verdadeira

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 10

#EXEMPLO 1

numero = -10
while numero < 10:
    print(numero)
    #numero = numero + 1

# OBS: Em um loop while, é importante que cuidemos do criterio de parada para não causar um loop infinito
"""

# Exemplo 2

resposta = ''

while resposta != 'sim':
    reposta = input('Ja acabou jessica ? ')
