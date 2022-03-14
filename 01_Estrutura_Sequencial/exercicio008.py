"""
008
Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

"""

ganho_por_hora, numero_de_horas = input("""Este programa calcula o salário 
    a partir do valor de hora e da quantidade de horas trabalhadas.
    Entre com o valor da hora e o a quantidade de horas separadas
    por vírgula.
    """).split(',')

print(f'O valor recebido por {int(numero_de_horas)} trabalhadas é de R$ {int(ganho_por_hora) * int(numero_de_horas)}.')
