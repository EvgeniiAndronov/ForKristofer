"""
Установив "Таблица символов GNOME"(gucharmap), найти в ней группу
"математические буквы и цифры"и вывести (в 10чном и 16-ом)
 в одну стоку список символов в этой группе и посчитать их?
 Далее в одну строчку выведите длину всей таблицы на сегодня (пусть 14 версия)?
"""

import unicodedata


class Num_51:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.count_symb = 0

    def count_symbols(self):
        for code in range(self.start, self.end + 1):
            try:
                unicodedata.name(chr(code))
                self.count_symb += 1
                print(chr(code))
            except ValueError:
                continue

    def info(self):
        print(self.count_symb)


if __name__ == '__main__':
    ob = Num_51(0x1D400, 0x1D7FF)
    ob.count_symbols()
    ob.info()
