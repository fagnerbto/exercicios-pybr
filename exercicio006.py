"""
006 
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
import math


raio = int(input('Este programa calcula a área de um círculo. Entre com o valor de raio desejado:'))

area = math.pi * (raio **2)

print(f'A área de um círculo de raio {raio} é {area}')
