import numpy as np
import linal_helper


def cofactors(m: np.array) -> np.array:
    cofactors_matrix = np.empty_like(m, dtype=float)

    # Получаем размерность матрицы
    n = m.shape[0]

    for i in range(n):
        for j in range(n):
            # Создаем временную матрицу, удаляя i-ую строку и j-ый столбец
            temp_matrix = np.delete(np.delete(m, i, axis=0), j, axis=1)

            # Вычисляем минор и умножаем его на соответствующий знак
            cofactor = (-1) ** (i + j) * np.linalg.det(temp_matrix)

            # Присваиваем значение матрицы алгебраических дополнений
            cofactors_matrix[i, j] = cofactor
    return cofactors_matrix


if __name__ == "__main__":
    x, y, matrix = linal_helper.input_matrix()
    A = matrix.T[:y - 1].T
    print("Матрица коэффициентов:\n", A)
    B = matrix.T[y - 1: y].T
    print("Матрица свободных членов:\n", B)
    print()
    row_rank = np.linalg.matrix_rank(A)
    col_rank = np.linalg.matrix_rank(A.T)
    print("Ранг для строк:", row_rank)
    print("Ранг для столбцы:", col_rank)

    if row_rank == x:
        print("Т. к. строчный ранг равен количеству строк, то матрица правообратима")
        print("Считаем псевдообратную матрицу")
        S = A.dot(A.T)
        print("A * A.T = \n", S)
        S_det = np.linalg.det(S)
        print("Определитель матрицы A * A.T:", S_det)
        S_cofactors = cofactors(S)
        print("Матрица алгебраических дополнений:\n", S_cofactors)
        S_inv = S_cofactors.T / S_det
        print("(A * A.T)^-1 = \n", S_inv)
        A_pseudo = A.T.dot(S_inv)
        print("Псевдообратная к A матрица:")
        print("(A * A.T)^-1 * A.T = \n", A_pseudo)
        result = A_pseudo.dot(B)
        print("Псевдорешение: ")
        print(result)
    elif col_rank == y - 1:
        print("Т. к. столбцовый ранг равен количеству столбцов, то матрица левообратима")
        print("Считаем псевдообратную матрицу")
        S = A.T.dot(A)
        print("A.T * A = \n", S)
        S_det = np.linalg.det(S)
        print("Определитель матрицы A.T * A:", S_det)
        S_cofactors = cofactors(S)
        print("Матрица алгебраических дополнений:\n", S_cofactors)
        S_inv = S_cofactors.T / S_det
        print("(A.T * A)^-1 = \n", S_inv)
        A_pseudo = S_inv.dot(A.T)
        print("Псевдообратная к A матрица:")
        print("(A.T * A)^-1 * A.T = \n", A_pseudo)
        result = A_pseudo.dot(B)
        print("Псевдорешение: ")
        print(result)
"""
Тест для левообратимой матрицы:
5 4
1 2 2 8
1 1 1 4
1 2 2 6
1 0 -1 0
1 0 -1 -2

Тест для правообратимой матрицы:
2 4
1 2 2 8
1 1 1 4
"""
