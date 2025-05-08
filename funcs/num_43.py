"""
Дан текстовый файл, в каждой строчке по числу (интовое или флоат).
Через sys.argv найти в указанном файле и вывести макс и мин число и номера их строк?
"""

import sys

filename = sys.argv[1]


def num_43():
    with open(filename) as f:
        lines = f.readlines()

    new_list = []

    for line in lines:
        new_list.append(float(line))

    max_num = max(new_list)
    max_id = new_list.index(max_num)
    min_num = min(new_list)
    min_id = new_list.index(min_num)

    print(f"max: {max_num},\t min: {min_num}\nline max: {max_id},\t line min: {min_id}")


if __name__ == "__main__":
    num_43()
