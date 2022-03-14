"""
012
Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = float(input('Forneça a sua altura para que o programa calcule seu peso ideal:'))


peso_ideal = (altura * 72.7) - 58

print(f'Seu peso ideal é de {peso_ideal}')