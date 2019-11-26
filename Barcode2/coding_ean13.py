#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Вторая попытка реализации EAN 13 в Python конветируя алгоритм из Delphi
"""

def create_ean13_succession(a_namber_uan):
    """ Кортежи list_A list_B list_C  list_AB используются для преобразования цифр в штрихи.
        0 — прозрачный штрих;
        1 — черный штрих.
        Вся последовательность штрихов начинается и заканчивается последовательностью «101».
        1-я цифра используется для кодировки цифр с 2-й по 7-ю.
        Далее из кортежа  list_AB выбираетя элемент с индексом, равным значению 1-й цифры и
        из этого элемента выбирается символ с индексом, равным номеру позиции 2-7 цифры минус 1.
        Если символ равен «A», то выбираем поледовательность с индексом, равным значению 2-7
        цифры соответственно из кортежа list_A.
        Если символ равен «B», то выбираем последовательность с индексом, равным значению 2-7
        цифры соответственно из кортежа list_B.
        Полученная последовательность добавляется к общей.
        Далее добавляется разделительные штрихи «01010».
        Штрихи для цифр с 8-й по 13-ю берутся по индексу, равным значению соответствующий
        цифре из кортежа  list_C.
        :param a_namber_uan: значение штрих-кода
        :return: последовательность 0 и 1.
    """
    list_A = ('0001101', '0011001', '0010011', '0111101', '0100011',
              '0110001', '0101111', '0111011', '0110111', '0001011')
    list_B = ('0100111', '0110011', '0011011', '0100001', '0011101',
              '0111001', '0000101', '0010001', '0001001', '0010111')
    list_C = ('1110010', '1100110', '1101100', '1000010', '1011100',
              '1001110', '1010000', '1000100', '1001000', '1110100')
    list_AB = ('AAAAAA', 'AABABB', 'AABBAB', 'AABBBA', 'ABAABB',
               'ABBAAB', 'ABBBAA', 'ABABAB', 'ABABBA', 'ABBABA')

    # начало штрихкода
    result = "101"
    # добавление штрихов с 3-й по 7-ю цифры
    element_AB = list_AB[int(a_namber_uan[0])]
    for pos in range(2, 8):
        char = element_AB[pos-2]
        if char == "A":
            result += list_A[int(a_namber_uan[pos-1])]
        elif char == "B":
            result += list_B[int(a_namber_uan[pos-1])]
    # добавление разделительных штрихов
    result += "01010"
    # добавление штрихов с 8-й по 13-ю цифры
    for pos in range(8, 14):
        result += list_C[int(a_namber_uan[pos - 1])]
    # завершение последовательности штрихов
    result += "101"

    print(result)


# number_ean13 = "077511997181"
number_ean13 = "4820207340015"
create_ean13_succession(number_ean13)
