"""
создать рандомн список из 20 целых (1,12) и срезами скопировать его в другой с конца через два?
"""

import random

def num_8():
    list_nums = []

    for _ in range(20):
        list_nums.append(random.randint(1, 12))

    print(list_nums)

    new = list_nums[::-2]
    print(new)

if __name__ == '__main__':
    num_8()