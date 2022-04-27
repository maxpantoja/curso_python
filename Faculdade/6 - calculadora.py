print('=== Este programa realiza operações entre dois números fornecidos pelo o usuário ===')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
oper = int(input('ESCOLHA UMA DAS OPERAÇÕES DIGITANDO SEU NÚMERO:\n(1)SOMA\n(2)SUBTRAÇÃO\n(3)MULTIPLICAÇÃO\n('
                 '4)DIVISÃO\nOPÇÃO: '))
if oper == 1:
    print(f'{n1} + {n2} = {n1 + n2}')
elif oper == 2:
    print(f'(n1-n2) {n1} - {n2} = {n1 - n2}\n(n2-n1) {n2} - {n1} = {n2 - n1}')
elif oper == 3:
    print(f'{n1} x {n2} = {n1*n2}')
elif oper == 4:
    if n2 != 0:
        print(f'(n1/n2) {n1} / {n2} = {n1/n2}')
    else:
        print('Impossível fazer n1/n2, tendo em vista que n2=0')
    if n1 != 0:
        print(f'(n2/n1) {n2} / {n1} = {n2/n1}')
    else:
        print('Não é possível dividir por 0')
