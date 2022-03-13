"""
04 - Programa que calcula a média anual a partir das notas fornecidas para cada
um dos 4 bimestres.
"""

bimestres = input("Forneça os valores para os 4 bimestres separados por vírgula:").split(',' )

resultado = (int(bimestres[0]) + int(bimestres[1]) + int(bimestres[2]) + int(bimestres[3]))/4

print(resultado)