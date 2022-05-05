# Faça um programa que leia uma frase pelo teclado e mostre:
# 1 - Quantas vezes a letra "A" aparece
# 2 - Em que posição ela aparece a primeira vez
# 3 - Em que posição ela aparece a última vez
frase = str(input('Escreva uma frase: ')).strip()
print(f'A quantidade de letra "A" que aparece no seu texto é: {frase.lower().count("a")}')
print(f'A posição em que ela aparece pela primeira vez é na: {frase.lower().find("a") + 1}')
print(f'A posição em que ela aparece pela última vez é na: {frase.lower().rfind("a") + 1}')