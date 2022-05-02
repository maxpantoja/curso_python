teste = 1
while teste == 1:
    n = int(input('Entre com o valor para saber a sua tabuada: '))
    print()
    i = 1
    while i <= 10:
        r = n * i
        print('%2d x %2d =%3d' % (n, i, r))
        i = i + 1
    teste = int(input('\nVocê deseja saber outra tabuada?\n(1)Sim\n(2)Não\nResposta: '))
