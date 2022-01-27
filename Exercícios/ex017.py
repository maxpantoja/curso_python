from math import sqrt
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#De um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
print('Preencha os dados em metros dos catetos para descobrir a hipotenusa de um triângulo retângulo!')
catetoo = float(input('Digite o comprimento do cateto oposto: '))
catetoa = float(input('Digite o comprimento do cateto adjacente: '))
hipo = sqrt(catetoo ** 2 + catetoa ** 2)
print(f'A hipotenusa deste triângulo retângulo mede {hipo:.2f}m')
