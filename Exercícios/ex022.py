# Crie um programa que leia o nome compleo de uma pessoa e mostre:
# 1 - O nome com todos as letras maiúsculas
# 2 - O nome com todas as letras minúsculas
# 3 - Quantas letras ao todo (sem coiderar espaços)
# 4 - Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
x = len(nome)
y = nome.count(' ')
print(nome.upper())
print(nome.lower())
print(f'O total de letras sem considerar espaços é {x - y}')
print(f'O total de letras do primeiro nome é {nome.find(" ")}')