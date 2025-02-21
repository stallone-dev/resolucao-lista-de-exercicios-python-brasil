"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido
Mostrar os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_15_clt_onerosa
    >>> numeros =['80', '55.62']
    >>> ex_15_clt_onerosa.input = lambda k: numeros.pop()
    >>> ex_15_clt_onerosa.calcular_assalto_no_salario()
    + Salário Bruto : R$ 4449.60
    - IR (11%) : R$ 489.46
    - INSS (8%) : R$ 355.97
    - Sindicato (5%) : R$ 222.48
    = Salário Liquido : R$ 3381.70

"""


def calcular_assalto_no_salario() -> None:
    salario_hora = float(input("Salário hora: "))
    horas_trabalhadas = float(input("Horas trabalhadas: "))

    TAXA_IR = 0.11
    TAXA_INSS = 0.08
    TAXA_SINDICATO = 0.05

    bruto = salario_hora * horas_trabalhadas
    pag_ir = bruto * TAXA_IR
    pag_inss = bruto * TAXA_INSS
    pag_sindicato = bruto * TAXA_SINDICATO
    liquido = bruto - pag_ir - pag_inss - pag_sindicato

    print(f"+ Salário Bruto : R$ {bruto:.2f}")
    print(f"- IR (11%) : R$ {pag_ir:.2f}")
    print(f"- INSS (8%) : R$ {pag_inss:.2f}")
    print(f"- Sindicato (5%) : R$ {pag_sindicato:.2f}")
    print(f"= Salário Liquido : R$ {liquido:.2f}")
