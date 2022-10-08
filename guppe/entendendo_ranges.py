"""
Ranges
-Precisamos conhecer o loop for para utilizar os ranges.
-Precisamos conhecer o range para trabalhar melhor com os loops for.

Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria, mas sim de maneira expecificada.

Forma gerais:

#Forma 1

range(valor_de_para)

OBS: valor_de_para não inclusive (inicio padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

#Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_para não inclusive (inicio especificado pelo usuario, e passo de 1 em 1)

#Exemplo forma 2

for num in range(4,11):
    print(num)

#Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_para não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)
#Exemplo forma 3
for num in range(5, 55, 5):
    print(num)

#Forma 4 (Inversa)
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_para não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)
"""
# Exemplo forma 4
for num in range(10, 0, -1):
    print(num)
