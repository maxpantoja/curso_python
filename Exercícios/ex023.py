# Faça um programa que leia um número de 0 a 9999 e motre na tela cada um dos dígitos separados
# Ex: Digite um número: 1834
# Unidade:4 / Dezena: 3 / Centena: 8 / Milhar: 1
n = int(input('Digite um número inteiro de 0 a 9999: '))
print(f'Milhar: {int(n/1000)}\nCentena: {int(n/1000) * 1000 - int(n/100)}')

