import numpy as np
import matplotlib.pyplot as plt

nesting_level = 0


def tab() -> str:
    return "\t" * nesting_level


def in_sub_problem(sign):
    global nesting_level
    print("\n")
    print(tab(), end="")
    print("-" * 20)
    nesting_level += 1
    display(sign)


def out_sub_problem():
    global nesting_level
    nesting_level -= 1
    print(tab(), end="")
    print("-" * 20)
    print("\n")


def display(*args):
    for i in range(len(args)):
        if type(args[i]) == np.ndarray:
            if i != 0:
                print()
            display_matrix(args[i])
        else:
            display_value(args[i], end="")
    print()


def display_value(value, end="\n"):
    print(f'{tab()}{value}', end=end)


def display_matrix(matrix: np.ndarray):
    for row in matrix:
        print(tab(), *row)
