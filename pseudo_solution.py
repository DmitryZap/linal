import numpy as np
import linal_helper
import display_helper

if __name__ == "__main__":
    x, y, matrix = linal_helper.input_matrix()

    A = matrix.T[:y - 1].T
    display_helper.display("Матрица коэффициентов A = ", A)

    B = matrix.T[y - 1: y].T
    display_helper.display("Матрица свободных членов B = ", B)

    row_rank, col_rank = linal_helper.full_rank(A, "A")

    if row_rank == x:
        display_helper.in_sub_problem("Т. к. строчный ранг равен количеству строк, то матрица правообратима")
        display_helper.display("Считаем псевдообратную матрицу")

        S = A.dot(A.T)
        display_helper.display("S = A * A.T = ", S)

        S_inv = linal_helper.inverse(S, "S")

        A_pseudo = A.T.dot(S_inv)
        display_helper.display("Псевдообратная матрица A^+ = A^t * S^-1 = ", A_pseudo)

        X = A_pseudo.dot(B)
        display_helper.display("Псевдорешение X^* = A^+ * B = ", X)

        display_helper.out_sub_problem()
    elif col_rank == y - 1:
        display_helper.in_sub_problem("Т. к. столбцовый ранг равен количеству столбцов, то матрица левообратима")
        display_helper.display("Считаем псевдообратную матрицу")

        S = A.T.dot(A)
        display_helper.display("S = A.T * A = ", S)

        S_inv = linal_helper.inverse(S, "S")

        A_pseudo = S_inv.dot(A.T)
        display_helper.display("Псевдообратная матрица A^+ = S^-1 * A^t = ", A_pseudo)

        X = A_pseudo.dot(B)
        display_helper.display("Псевдорешение X^* = A^+ * B = ", X)

        display_helper.out_sub_problem()
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
