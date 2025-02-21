"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

    >>> from secao_01_estrutura_sequencial import ex_16_loja_de_tintas_simples
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '50'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 1 lata(s) de tinta ao custo de R$ 80.00
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '100'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 2 lata(s) de tinta ao custo de R$ 160.00


"""

import math

def calcular_latas_e_preco_de_tinta() -> None:
    VOLUME_LATA_TINTA = 18.0
    M2_POR_LITRO_DE_TINTA = 3.0
    PRECO_LATA = 80.0

    area_a_pintar = float(input("Área a ser pintada: "))

    litros_necessarios = area_a_pintar / M2_POR_LITRO_DE_TINTA
    qnt_latas_necessarias = math.ceil(litros_necessarios / VOLUME_LATA_TINTA)
    custo_latas = qnt_latas_necessarias * PRECO_LATA

    print(f"Você deve comprar {qnt_latas_necessarias:.0f} lata(s) de tinta ao custo de R$ {custo_latas:.2f}")
