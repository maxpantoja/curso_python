print('Este programa irá mostrar a sua nota final.')
tl = float(input('Digite sua nota no trabalho de laboratório: '))
avs = float(input('Digite sua nota na Avaliação Semestral: '))
ef = float(input('Digite sua nota no exame final: '))
tl = tl*2
avs = avs*3
ef = ef*5
nota = (tl+avs+ef)/10
if nota < 5:
    print('Seu conceito foi igual a E')
elif 5 <= nota < 6:
    print('Seu conceito foi igual a D')
elif 6 <= nota < 7:
    print('Seu conceito foi igual a C')
elif 7 <= nota < 8:
    print('Seu conceito foi igual a B')
else:
    print('Sua conceito foi igual a A')

print(f'Sua nota final é {nota}')
