# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = str(input('Digite seu nome: ')).strip()
print(f'A afirmação de que este nome tem "Silva" é: {"silva" in nome.lower()}')
