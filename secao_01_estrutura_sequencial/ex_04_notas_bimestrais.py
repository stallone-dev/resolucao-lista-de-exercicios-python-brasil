"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media()
    A média anual é 8.5

"""


from typing import List

def calcular_media() -> None:
    nota_1 = int(input("Digite a 1º nota "))
    nota_2 = int(input("Digite a 2º nota "))
    nota_3 = int(input("Digite a 3º nota "))
    nota_4 = int(input("Digite a 4º nota "))
    media:float = (nota_1 + nota_2 + nota_3 + nota_4) / 4

    print(f"A média anual é {str(media)}")
