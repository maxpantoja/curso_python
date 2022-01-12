dias = int(input('Por quantos dias o carro foi usado: '))
km = float(input('Quantos Km o carro rodou: '))
total = (dias * 60) + (km * 0.15)
print(f'O total a ser pago é R${total:.2f}')
