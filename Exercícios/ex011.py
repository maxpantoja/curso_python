#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
#que cada litro de tinta pinta uma área de 2m^2

largura = float(input('Qual a largura em metros de sua parede? '))
altura = float(input('Qual a altura em metros de sua parede? '))
area = largura * altura
print(f'Sua área é de {area}m²')
print(f'Sabendo que cada litro de tinta pinta 2m², serão necessários {area / 2:.2f} litros, para pintar toda a parede.')
