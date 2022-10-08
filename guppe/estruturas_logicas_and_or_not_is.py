"""
Estuturas logicas: and(e), or(ou), not(não), is(é)

 -Operadores Unarios:
      -not, is
 -Operadores Binarios:
      -and, or

-Regras de funcionamento
Para o "and", ambos os valores precisam ser True
ativo = True
logado = True

if ativo and logado:
    print('Bem vindo usuario!')
else:
    print("Você precisa ativar sua conta. Por favor cheque seu e-mail")

Para o "or", um ou outro valor precisa ser True
ativo = True
logado = False

if ativo or logado:
    print('Bem vindo usuario!')
else:
    print("Você precisa ativar sua conta. Por favor cheque seu e-mail")

Para o 'not' o valor do bopoleano é invertido, ou seja se for True vira False se for False vira True
Para o 'is' o valor é comparado com um segundo

"""


ativo = True
logado = False

#se não estiver ativo
if not ativo:
    print('voce precisa ativar sua conta por favor cheque seu e-mail')
else:
    print('Bem vindo usuario')



