print('Este programa classifica em ordem decrescente os valores fornecidos.')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
# Encontra o número maior
max = n1
if n2 > max:
    max = n2
if n3 > max:
    max = n3
# Encontra o número menor
min = n1
if n2 < min:
    min = n2
if n3 < min:
    min = n3
# Encontra o número do meio
if max > n1 > min:
    mid = n1
elif max > n2 > min:
    mid = n2
else:
    mid = n3

print(f'Ordem decrescente: {max}, {mid}, {min}')
