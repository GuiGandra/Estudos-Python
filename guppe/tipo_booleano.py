"""
Tipo Booleano

Algebra booleana, criada por George boole

2 contantes, verdadeiro ou falso
True -> Verdadeiro
False -> Falso

OBS: SEMPRE COM A INICIAL MAIUSCULA

Errado: true, false

Certo: True, False

"""

ativo = True



print(ativo)

"""
Operações basicas:
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado sera falso,
se o for falso o resultado sera verdadeiro. Ou seja, sempre ao contrario.
 
"""
print(not ativo)

logado = False

# Ou (or):
"""
É uma operação binaria, ou seja, depende de outros valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):

"""
Tambem é uma operação binaria, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""