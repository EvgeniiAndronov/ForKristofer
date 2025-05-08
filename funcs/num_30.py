"""
задать список из 100 рандомных (0, 50) и вывести сколько чисел в каждом десятке
"""

import random


def num_30():
    list_nums = [random.randint(0, 50) for _ in range(100)]

    count_0_10 = 0
    count_10_20 = 0
    count_20_30 = 0
    count_30_40 = 0
    count_40_50 = 0

    for num in list_nums:
        if num < 10:
            count_0_10 += 1
        elif num < 20:
            count_10_20 += 1
        elif num < 30:
            count_20_30 += 1
        elif num < 40:
            count_30_40 += 1
        elif num <= 50:
            count_40_50 += 1

    print(
        f"0 - 9: {count_0_10}\n10 - 19: {count_10_20}\n20 - 29: {count_20_30}\n30 - 39: {count_30_40}\n40 - 50: {count_40_50}")


if __name__ == "__main__":
    num_30()
