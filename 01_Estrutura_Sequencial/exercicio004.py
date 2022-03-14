"""
004
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

bimestres = input("Forneça os valores para os 4 bimestres separados por vírgula:").split(',' )

resultado = (int(bimestres[0]) + int(bimestres[1]) + int(bimestres[2]) + int(bimestres[3]))/4

print(resultado)