#frase = 'Curso em Vídeo Python'

# print(frase[9:21:2])  Pega um intervalo desejado
# print(len(frase))  Pega a quantidade de caracter na frase
# print(frase.count('o')) Conta a quantidade vezes que a str se repete. Se colocar vísgula, da pra definir o intevalo
# print(frase.find('deo'))  Mostra onde está localizado o começo da str. Se n encontrar, irá mostrar "-1"
# print('Curso' in frase)  Confirma ou nega a presença da str desejada.
# print(frase.replace('Python', 'Android'))  Procura e substitue
# print(frase.upper())  Coloca a str toda em MAIÚSCULA
# print(frase.lower())  Coloca a str toda em MINÚSCULA
# print(frase.capitalize())  Deixa só a primeira letra MAIÚSCULA
# print(frase.title())  Todos os inicios de palavras MAIÚSCULOS
# print(frase.split())  Dividi a frase em palavras diferentes. Coloca dentro de uma lista (DAR UMA ESTUDADA)
# print('-'.join(frase))  Ele junta uma lista que está separada pelo split

#frase2 = '   Aprenda Python  '
# print(frase2.strip())  Remove os espaços excedentes da str. Do início e do final
# print(frase2.rstrip())  Remove só os espaços da direita
# print(frase2.lstrip()) Remove só os espaços da esquerda
texto = 'Curso em Vídeo Python'
print(texto[0::2])
'Curso' in texto
#print(texto.lower().count('o'))
print(len(texto.strip()))
print(texto.replace('Python', 'Android'))
print(texto.lower().find('vídeo'))

dividido = texto.split()
print(dividido[3][5])



#print("""Cavalo de troia rapsdsiaodfuilf huhhoç cs
#dsadsadsad ciuhsahcsachsca ccjjcojoasija~cscs
#afsafsalhfashiahsfhsaihoç""")


