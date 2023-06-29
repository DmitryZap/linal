import numpy as np

import linal_helper

if __name__ == "__main__":
    first_type = int(input("Выберите тип для первого подпространства: "))
    second_type = int(input("Выберите тип для второго подпространства: "))

    if first_type == 1:
        first = linal_helper.input_matrix()
    elif first_type == 2:
        first = linal_helper.input_linear_convex()

    if second_type == 1:
        second = linal_helper.input_matrix()
    elif second_type == 2:
        second = linal_helper.input_linear_convex()
