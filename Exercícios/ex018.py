from math import cos, sin, tan, radians
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
#desse ângulo
ang = int(input('Digite um ângulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f'O ângulo {ang}º tem o SENO de {seno:.2f}')
print(f'O ângulo {ang}º tem o COSSENO de {cosseno:.2f}')
print(f'O ãngulo {ang}º tem a TANGENTE de {tangente:.2f}')

