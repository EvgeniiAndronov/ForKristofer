"""
Установив "Таблица символов GNOME"(gucharmap), найти в ней группу
"математические буквы и цифры"и вывести (в 10чном и 16-ом)
 в одну стоку список символов в этой группе и посчитать их?
 Далее в одну строчку выведите длину всей таблицы на сегодня (пусть 14 версия)?
"""

import unicodedata

start_addr = 0x1D400
end_addr = 0x1D7FF

count_symbols = 0

for code in range(int(start_addr), int(end_addr) + 1):
    try:
        unicodedata.name(chr(code))
        count_symbols += 1
        print(unicodedata.name(chr(code)))
    except ValueError:
        continue

print(count_symbols)
