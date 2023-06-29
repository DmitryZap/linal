import numpy as np
import scipy as sp

import display_helper


def input_matrix() -> (int, int, np.ndarray):
    matrix = []

    x, y = map(int, input("Введите количество строк и столбцов: ").split())

    print("Введите расширенную матрицу системы:")
    for i in range(x):
        matrix.append(list(map(float, input().split())))
    matrix = np.array(matrix)
    return x, y, matrix


def input_linear_convex() -> (int, np.ndarray, np.ndarray):
    dim = int(input("Введите размерность: "))
    point = list(map(float, input("Введите точку: ").split()))
    vector_amount = int(input("Введите количество векторов в линейной оболочке: "))

    convex = []

    for i in range(vector_amount):
        convex.append(list(map(float, input().split())))

    point = np.array(point)
    convex = np.array(convex)

    return dim, point, convex


def full_rank(matrix: np.ndarray, name="M") -> (int, int):
    display_helper.in_sub_problem("Посчитаем столбцовый и строчный ранг:")

    row_rank = np.linalg.matrix_rank(matrix)
    col_rank = np.linalg.matrix_rank(matrix.T)
    display_helper.display(f"rank_row({name}) = ", row_rank)
    display_helper.display(f"rank_col({name}) = ", col_rank)

    display_helper.out_sub_problem()
    return row_rank, col_rank


def cofactors(matrix: np.array) -> np.array:
    cofactors_matrix = np.empty_like(matrix, dtype=float)

    # Получаем размерность матрицы
    n = matrix.shape[0]

    for i in range(n):
        for j in range(n):
            # Создаем временную матрицу, удаляя i-ую строку и j-ый столбец
            temp_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)

            # Вычисляем минор и умножаем его на соответствующий знак
            cofactor = (-1) ** (i + j) * np.linalg.det(temp_matrix)

            # Присваиваем значение матрицы алгебраических дополнений
            cofactors_matrix[i, j] = cofactor
    return cofactors_matrix


def inverse(M: np.array, name="M") -> np.array:
    display_helper.in_sub_problem(f"Посчитаем матрицу {name}^-1")

    M_det = np.linalg.det(M)
    display_helper.display("det({name}) = ", M_det)

    M_cofactors = cofactors(M)
    display_helper.display(f"Матрица алгебраических дополнений {name}^* = ", M_cofactors)

    M_inv = M_cofactors.T / M_det

    display_helper.display(f"{name}^-1 = (1/det{name}) * {name}^*t", M_inv)

    display_helper.out_sub_problem()
    return M_inv


def matrix2convex(x: int, y: int, matrix: np.ndarray) -> (int, np.array, np.array):
    _, _, U = sp.linalg.lu(matrix)

    print(U)

    A = U.T[:y - 1].T
    B = U.T[y - 1: y].T

    print(A)

    print(B)

    F = A.T.copy()
    deleted = 0
    is_bounded = True
    for i in range(len(A.T)):
        for j in range(len(A.T[i])):
            if i == j and A.T[i][j] != 1:
                is_bounded = False
                break
            elif i != j and A.T[i][j] != 0:
                is_bounded = False
                break
        if not is_bounded:
            break
        F = np.delete(F, i - deleted, axis=0)
        deleted += 1

    F = F.T
    print(F)

    point = B - F.dot(np.ones((x, 1)))
    print(point)
