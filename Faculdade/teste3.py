cont = 0
num = int(input('Digite o número inicial: '))
num2 = int(input('Digite o número final: '))
while num <= num2:
    if num % 2 == 0:
        cont = cont + num
    num = num + 1
print(cont)
