"""
015
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
* salário bruto.
* quanto pagou ao INSS.
* quanto pagou ao sindicato.
* o salário líquido.
* calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""

ganho_por_hora, numero_de_horas = input("""Este programa calcula o salário 
    a partir do valor de hora e da quantidade de horas trabalhadas.
    Entre com o valor da hora e o a quantidade de horas separadas
    por vírgula.
    """).split(',')

ganho_por_hora, numero_de_horas = float(ganho_por_hora),int(numero_de_horas)

IR = 11/100
INSS = 8/100
SINDICATO = 5/100

salario_bruto = ganho_por_hora * numero_de_horas
imposto_de_renda = salario_bruto - (salario_bruto * (1 - IR))
inss = salario_bruto - (salario_bruto * (1-INSS))
sindicato = salario_bruto - (salario_bruto * (1-SINDICATO))

salario_liquido = salario_bruto - imposto_de_renda - inss - sindicato
print(f'Salário Bruto: R$ {salario_bruto}')
print(f'Desconto de Imposto de Renda: R$ {imposto_de_renda}')
print(f'Desconto INSS: R$ {inss}')
print(f'Desconto sindicato: R$ {sindicato}')
print(f'Salário Líquido: R${salario_liquido}')
