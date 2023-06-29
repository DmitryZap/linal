import numpy as np
import linal_helper
import math

if __name__ == "__main__":
    # Ввод данных
    dim1, point1, convex1 = linal_helper.input_linear_convex()
    dim2, point2, convex2 = linal_helper.input_linear_convex()

    # Вывод первоначальных данных
    print("Точка A1:", point1)
    print("Линейная оболочка V1: ")
    print(convex1)
    print("Точка A2:", point2)
    print("Линейная оболочка V2: ")
    print(convex2)

    # Составляем матрицу, где столбцы -- это веткторы первой и второй линейных оболочек
    P = np.c_[convex1, convex2]
    print("Матрица P: ")
    print(P)

    # Вычитаем координаты точки A1 из A2
    pointDiffs = np.diff([point2, point1], axis=0).T
    print("A2 - A1:")
    print(pointDiffs)

    # Считаем P_tilda, добавляя A2 - A1 как последний столбец
    print("Матрица P_tilda = (M|A2 - A1): ")
    P_tilda = np.c_[P, pointDiffs]
    print(P_tilda)

    # Транспорнируем P_tilda
    print("P_tilda.T:")
    print(P_tilda.T)

    # Считаем P_tilda.T * P_tilda
    print("P_tilda.T * P_tilda:")
    P_tilda_T_dot_P_tilda = P_tilda.T.dot(P_tilda)
    print(P_tilda_T_dot_P_tilda)

    # Считаем определитель det(P_tilda.T * P_tilda)
    print("Определитель P_tilda.T * P_tilda: ")
    det_P_tilda_T_dot_P_tilda = np.linalg.det(P_tilda_T_dot_P_tilda)
    print(det_P_tilda_T_dot_P_tilda)

    # Транспонируем P:
    print("P.T:")
    print(P.T)

    # Считаем P.T * P
    print("P.T * P:")
    P_T_dot_P = P.T.dot(P)
    print(P_T_dot_P)

    # Считаем определитель det(P.T * P)
    print("Определитель P.T * P: ")
    det_P_T_dot_P = np.linalg.det(P_T_dot_P)
    print(det_P_T_dot_P)

    # Считаем расстояние
    result = math.sqrt(det_P_tilda_T_dot_P_tilda / det_P_T_dot_P)
    print(f"d = sqrt(det(P_tilda.T * P) / det(P.T * P)) = sqrt({det_P_tilda_T_dot_P_tilda} / {det_P_T_dot_P}) =", result)


"""
3 6
1 0 1 1 -2 2
0 1 1 -1 -1 3
1 -1 2 0 -1 3
"""

"""
3
2
1 -1 7 9 4
2
2 1 2 -1 1
0 1 2 1 2
3
2
-2 -1 2 0 0
2
0 2 -1 1 0
2 1 0 0 1
"""

"""
Норм тест
0
0
1 1 1 1 1
2
0 0 -1 0 1
1 0 0 0 0
0
0
-1 -1 -1 -1 -1
2
0 0 0 1 0
0 -1 1 -1 0
"""
