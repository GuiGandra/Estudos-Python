"""
Escopo de variaveis

1 - Variaveis Globais;
     - Variaveis Globas são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2- Variaveis locais:
    - Variaveis Locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo esta limitado
    ao bloco onde foi declarada.

Para declara variaveis em python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que
ao declararmos uma variavel, nos não colocamos o tipo de dado dela.
Este tipo é inferido o atribuirmos o valor a mesma

Exemplo em C:
int numero = 42;

Exemplo em java:
int numero = 42;
"""
numero = 42 # Exemplo de variavel global
print(numero)
print(type(numero))

numero = 'Gandra'
print(numero)
print(type(numero))

nao_existo = 'G'
print(nao_existo)

numero = 42
novo = 0
if numero > 10:
    novo = numero + 10 # A variavel 'novo' esta declarada localmente dentro do bloco if. Portanto é local
    print(novo)


