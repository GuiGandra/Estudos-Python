"""
Tipo String

Em Python, um dado é considerado tipo string sempre que:

- Estiver em aspas simples -> 'Umas string', '234', 'a', 'True', '42.3'.
- Estiver em aspas Duplas -> "Umas string", "234", "a", "True", "42.3".
- Estiver em aspas simples triplas -> '''Umas string''', '''234''', '''a''', '''True''', '''42.3'''.
nome = 'Guilheme'
print(nome)
print(type(nome))

nome = "Gandra's Bar"
print(nome)
print(type(nome))

nome = 'Guilherme \nGandra'
print(nome)
print(type(nome))

nome = "Guilherme \" Gandra"
print(nome)
print(type(nome))
           \ -> Caracter de escape

           print(nome.upper()) -> DEIXA AS LETRAS MAIUSCULAS
           print(nome.lower()) -> DEIXA AS LETRAS minusculas
           print(nome.split()) -> TRANSFORMA EM UMA LISTA DE STRINGS

# [  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14,  15]
# [ 'G', 'u', 'i', 'l', 'h', 'e', 'r', 'm', 'e', '  ', 'G', 'a', 'n', 'd', 'r', 'a']
nome = 'Guilherme Gandra'
print(nome[0:10]) # Slice de string
print(nome[10:17]) # Slice de string
# [      0,          1  ]
# [ 'Guilherme', 'Gandra]
print(nome.split()[0])
print(nome.split()[1])

print(nome[15], nome[0], nome[1], nome[2]) -> ESCOLHER AS LETRAS
"""

#- Estiver em aspas Duplas triplas -> """Umas string""", """234"""", """a"""", """True"""", """42.3""".
# [  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14,  15]
# [ 'G', 'u', 'i', 'l', 'h', 'e', 'r', 'm', 'e', '  ', 'G', 'a', 'n', 'd', 'r', 'a']

"""
[::-1] comece do primeiro elemento va ate o ultimo elemento e inverta (PALAVRA AO CONTRARIO)
"""
nome = 'Guilherme Gandra'
print(nome[::-1]) # Inversão da string Pythonico
print(nome.replace('G', 'P')) # Troca de letra

texto = 'socorram me subino onibus em marrocos' #Pálindromo
print(texto)
print(texto[::-1])

nome = 'ana' #Pálindromo
print(nome)
print(nome[::-1])


