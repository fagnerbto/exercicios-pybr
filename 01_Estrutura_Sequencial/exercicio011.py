"""
011
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
* o produto do dobro do primeiro com metade do segundo .
* a soma do triplo do primeiro com o terceiro.
* o terceiro elevado ao cubo.
"""
primeiro = int(input('Entre com um número inteiro:'))
segundo = int(input('Entre com outro número inteiro:'))
terceiro = float(input('Entre com um número real:'))

print(f'Calculando o produto de 2 x {primeiro} com metade de {segundo}. Resultando em {(2*primeiro) * (segundo/2)}')
print(f'A soma do triplo de {primeiro} com {terceiro}. Resultando em { 3*primeiro + terceiro }')
print(f'{terceiro} elevado ao cubo. Resultando em {terceiro ** 3}')