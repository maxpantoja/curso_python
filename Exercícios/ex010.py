#Crie um programa que leia quanto deinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar (Considerar = 5,63)
valor = float(input('Digite um valor em Real para verificar quantos dólares você pode comprar: R$'))
valord = valor / 5.63
print(f'Com o seu dinheiro atual, será possível comprar U${valord:.2f}')

