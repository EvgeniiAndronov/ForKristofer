"""
01. Зараз (на раз) создать словарь с ключами, которые есть числа
от 1 до 26 и значениями, которые есть буквы лат алфавита.
"""

from string import ascii_lowercase

dictionary = {i + 1: v for i, v in enumerate(ascii_lowercase)}

print(dictionary)
