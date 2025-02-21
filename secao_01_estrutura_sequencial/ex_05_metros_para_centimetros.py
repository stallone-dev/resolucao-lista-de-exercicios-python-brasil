"""
Exercício 05 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que converta metros para centímetros.

    >>> from secao_01_estrutura_sequencial import ex_05_metros_para_centimetros
    >>> ex_05_metros_para_centimetros.input = lambda k: '1'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centimetros()
    Transformando para centímetros dá 100.0 cm
    >>> ex_05_metros_para_centimetros.input = lambda k: '3.621'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centimetros()
    Transformando para centímetros dá 362.1 cm

"""


def converter_metros_para_centimetros() -> None:
    medida_em_metros = float(input("Insira o tamaho e metros: "))
    medida_em_cm = medida_em_metros * 100

    print(f"Transformando para centímetros dá {str(medida_em_cm)} cm")
