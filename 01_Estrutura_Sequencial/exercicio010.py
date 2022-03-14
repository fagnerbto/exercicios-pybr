"""
010
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

graus_celcius = int(input('Forneça um valor de temperatura em graus celcius e o programa converterá em graus Fahrenheit.'))

graus_fahrenheit = (graus_celcius * 1.8) + 32

print(f'Graus Celcius=>{graus_celcius} == Graus Fahrenheit => {graus_fahrenheit}')
