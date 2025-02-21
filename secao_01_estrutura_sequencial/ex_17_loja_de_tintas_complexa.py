"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""

import math


def calcular_latas_e_preco_de_tinta() -> None:
    M2_POR_LITRO = 6.0

    VOLUME_LATA = 18.0
    PRECO_LATA = 80.0

    VOLUME_GALAO = 3.6
    PRECO_GALAO = 25.0

    MARGEM_ERRO = 0.1

    area_a_pintar = math.ceil(
        float(input("Área a ser pintada: ")) * (1.0 + MARGEM_ERRO)
    )

    litros_necessarios = area_a_pintar / M2_POR_LITRO

    rendimento_lata = VOLUME_LATA * M2_POR_LITRO
    rendimento_galao = VOLUME_GALAO * M2_POR_LITRO

    qnt_latas_necessarias = math.ceil(area_a_pintar / rendimento_lata)
    qnt_galoes_necessarios = math.ceil(area_a_pintar / rendimento_galao)

    custo_latas = qnt_latas_necessarias * PRECO_LATA
    custo_galoes = qnt_galoes_necessarios * PRECO_GALAO

    equilibrio_lata = math.floor(area_a_pintar / rendimento_lata)
    equilibrio_galao = math.ceil((area_a_pintar % rendimento_lata) / rendimento_galao)
    custo_equilibrio = equilibrio_lata * PRECO_LATA + equilibrio_galao * PRECO_GALAO

    print(f"Você deve comprar {litros_necessarios:.0f} litros de tinta.")
    print(
        f"Você pode comprar {qnt_latas_necessarias:.0f} lata(s) de 18 litros a um custo de R$ {custo_latas:.0f}. Vão sobrar {(qnt_latas_necessarias * VOLUME_LATA - litros_necessarios):.1f} litro(s) de tinta."
    )
    print(
        f"Você pode comprar {qnt_galoes_necessarios:.0f} lata(s) de 3.6 litros a um custo de R$ {custo_galoes:.0f}. Vão sobrar {(qnt_galoes_necessarios * VOLUME_GALAO - litros_necessarios):.1f} litro(s) de tinta."
    )
    print(
        f"Para menor custo, você pode comprar {equilibrio_lata:.0f} lata(s) de 18 litros e {equilibrio_galao:.0f} galão(ões) de 3.6 litros a um custo de R$ {custo_equilibrio:.0f}. Vão sobrar {(equilibrio_lata * VOLUME_LATA + equilibrio_galao * VOLUME_GALAO - litros_necessarios):.1f} litro(s) de tinta."
    )
