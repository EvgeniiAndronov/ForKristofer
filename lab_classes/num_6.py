"""
Через списковое включение и ранг вывести все четные числа в диапазоне -150, до 150 с шагом 5,
включая крайние точки, при этом профильтровать, чтобы не выводились кратные 20, также вывести
сколько их получилось таких чисел?
"""


class Num_6:
    def __init__(self, start, stop, step=5, diver=20):
        self.start = start
        self.stop = stop
        self.step = step
        self.diver = diver

    def create_list(self):
        listing = [i for i in range(self.start, self.stop, self.step) if i % self.diver == 0]

        return listing

    def info(self):
        listing = self.create_list()
        count_vals = len(listing)
        print(f"listing: {listing}\ncount_vals: {count_vals}")


if __name__ == "__main__":
    ob = Num_6(-150, 150)
    ob.info()
