from functools import reduce


def product(lst):
    return reduce(lambda a, b: a * b, lst, 1)

if __name__ == "__main__":
    print(product([1, 2, 3, 4]))
