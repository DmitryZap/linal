import numpy as np


def input_matrix() -> (int, int, np.array):
    matrix = []

    x, y = map(int, input("Введите количество строк и столбцов: ").split())

    print("Введите расширенную матрицу системы:")
    for i in range(x):
        matrix.append(list(map(float, input().split())))
    matrix = np.array(matrix)
    return x, y, matrix


def input_linear_convex() -> (int, np.array, np.array):
    dim = int(input("Введите размерность: "))
    point = list(map(float, input("Введите точку: ").split()))
    vector_amount = int(input("Введите количество векторов в линейной оболочке: "))

    convex = []

    for i in range(vector_amount):
        convex.append(list(map(float, input().split())))

    point = np.array(point)
    convex = np.array(convex)

    return dim, point, convex


def matrix2convex(x: int, y: int, matrix: np.array) -> (int, np.array, np.array):
    point = np.linalg.solve(matrix)
    matrix_tmp = matrix.copy()
    matrix_tmp = matrix_tmp.T
    matrix_tmp[y - 1] = np.zeros(x)
    convex = np.linalg.solve(matrix_tmp)
