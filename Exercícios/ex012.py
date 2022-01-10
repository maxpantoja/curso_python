#Faça um algoritimo que leia o preço de um produto e mostre seu novo
#preço, com 5% de desconto
preco = float(input('Digite o preço de um produto para aplicar desconto de 5%: R$'))
precod = (preco * 0.05 - preco) * -1
print(f'O preço do produto com desconto de 5% é: R${precod:.2f}')
