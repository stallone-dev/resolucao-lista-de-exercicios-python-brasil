"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1

"""


def ordenar_decrescente(x: float, y: float, z: float) -> None:
    """Escreva aqui em baixo a sua solução"""
    sort_list = sorted(list([x, y, z]), reverse=True)
    result = ""
    for index, item in enumerate(sort_list):
        if index < sort_list.__len__() - 1:
            result += f"{item}, "
        else:
            result += f"{item}"
    print(result)
