"""
013
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

altura = float(input('Forneça a sua altura para que o programa calcule seu peso ideal: '))
sexo = input('Forneça o seu gênero: F para feminino e M para masculino: ')[0].upper()

peso_ideal = (altura * 62.1) - 44.7

if sexo == 'M':
    peso_ideal = (altura * 72.7) - 58

print(f'Seu peso ideal, para o sexo {sexo}, é de {peso_ideal} kg.')


