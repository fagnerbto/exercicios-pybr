"""
009
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

graus_fahrenheit = int(input('Forneça um valor de temperatura em fahrenheit e o programa converterá em graus célcius.'))

graus_celcius = 5 * ((graus_fahrenheit -32)/ 9)

print(f'Graus Fahrenheit => {graus_fahrenheit} == Graus Celcius=>{graus_celcius}')
