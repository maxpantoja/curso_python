#faça um algoritmo que leia um salário de um funcionário e mostre seu
#novo salário, com 15% de aumento
valor = float(input('Digite o salário atual para aplicar aumento de 15%: R$'))
aumento = valor * 0.15 + valor
print(f'Seu novo salário com aumento de 15% é R${aumento:.2f}')
