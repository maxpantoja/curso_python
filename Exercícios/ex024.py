# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(f'A afirmação de que sua sidade começa com "Santo" é: {"santo" in cidade.lower().split()[0]}')