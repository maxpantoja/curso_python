print('Nova política na empresa!! Digite seu salário atual pra ver seus novos benefícios!')
sal = float(input('Salário Atual: R$'))
# Auxílio escola
if sal <= 600:
    aux = 150.00
else:
    aux = 100.00
# Aumento salarial
if sal <= 500:
    sal = sal * 1.05
    print(f'PARABÉNS! Seu novo salário é R${sal:.2f} + Auxílio escola de R${aux}')
elif sal <= 1200:
    sal = sal * 1.12
    print(f'PARABÉNS! Seu novo salário é R${sal:.2f} + Auxílio escola de R${aux}')
else:
    print(f'Infelizmente, ainda não foi liberado aumento para você. Mas ganhaste Auxílio escola no valor de R${aux}')