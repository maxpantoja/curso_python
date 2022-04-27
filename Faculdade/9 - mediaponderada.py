print('Este programa irá mostrar a sua nota final.')
tl = float(input('Digite sua nota no trabalho de laboratório: '))
avs = float(input('Digite sua nota na Avaliação Semestral: '))
ef = float(input('Digite sua nota no exame final: '))

tl = tl*2
avs = avs*3
ef = ef*5

print(f'Sua nota final é {(tl+avs+ef)/10}')