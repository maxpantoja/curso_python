import os
import sys

# Programa para calcular a média de 4 notas
print('=== Digite o valor de 4 notas para calcular a média ===')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
print(f'A média das notas é {media:.1f}')


sys.stdout.flush()
os.execv(sys.argv[0], sys.argv)
