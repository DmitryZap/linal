import numpy as np

import linal_helper

if __name__ == "__main__":
    first_type = int(input("Выберите тип для первого подпространства: "))
    # second_type = int(input("Выберите тип для второго подпространства: "))

    if first_type == 1:
        dim1, point1, convex1 = linal_helper.matrix2convex(*linal_helper.input_matrix())
    else:
        dim1, point1, convex1 = linal_helper.input_linear_convex()

    # print(dim1)
    # print(point1)

    # if second_type == 1:
    #     dim2, point2, convex2 = linal_helper.matrix2convex(*linal_helper.input_matrix())
    # else:
    #     dim2, point2, convex2 = linal_helper.input_linear_convex()

"""
3 6
1 0 1 1 -2 2
0 1 1 -1 -1 3
1 -1 2 0 -1 3
"""