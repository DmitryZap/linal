from sympy import *
import numpy

# def scalar_product(a: Matrix, b: Matrix):
#

def orthoganalize(vectors: list[Matrix]):
    orthonormalized = []
    for a in vectors:
        b = a.copy()
        for b_i in orthonormalized:
            s1 = symbols('s1')
            s2 = symbols('s2')
            expression = b - (s1/s2) * b_i
            print(expression)

            s1_value = b.dot(b_i)
            s2_value = b_i.dot(b_i)
            b = expression.subs(s1, s1_value).subs(s2, s2_value).evalf()
        orthonormalized.append(b)
    print(orthonormalized)


if __name__ == "__main__":
    amount = int(input())  # Количество векторов

    vectors = []

    for i in range(amount):
        vector = list(map(int, input().split()))
        vectors.append(Matrix(vector))

    orthoganalize(vectors)
