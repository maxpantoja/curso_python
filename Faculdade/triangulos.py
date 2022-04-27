def calculadora():
    A = float(input('Este programa verifica o tipo de triângulo através dos lados fornecidos. \nForneça o lado 1: '))
    B = float(input('Lado 2: '))
    C = float(input('Lado 3: '))

    if (A + B > C and A + C > B and B + C > A):
        if (A == B == C):
            print('Os lados fornecidos formam um triângulo EQUILÁTERO.')
        elif (A == B or A == C or B == C):
            print('Os lados fornecidos formam um triângulo ISÓSCELES.')
        else:
            print('Os lados fornecidos formam um triângulo ESCALENO.')
    else:
        con = int(input(
            'Os valores fornecidos NÃO FORMAM um triângulo.\nQue tal tentar novamente?\nDigite (1) para sim.\nDigite '
            '(2) para não.\nResposta: '))
        if (con == 1):
            print('\n' * 2)
            calculadora()
calculadora()









