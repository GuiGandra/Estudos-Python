"""
PEP8 - Python Enhancement Proposal
The Zen of Python
import this

A ideia da PEP8 é que possamos escrever Pythhon de forma Pythonica.

[1] - Utilize Camel Case para nomes de classes;
class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculo, separado por underline para funções ou variáveis;
def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para indentação! (NÃO USE O TAB)
if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas
# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não ha problemas um utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções
# Não faça:

funcao ( algo[ 1 ], { outro: 2} )

# Faça:

funcao (algo[1], {outro:2})

#Não faça:

algo (1)

# Faça

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

# Faça:

dict['chave'] = lista[indice]

# Não faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre um instrução com uma nova linha
"""
import this



