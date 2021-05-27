from program.objects.Matrix import Matrix

import numpy as np
import math
import timeit


class MatrixResolver:

    @staticmethod
    def __norm(residum):
        sum_norm = 0
        for y in range(len(residum)):
            sum_norm += residum[y] ** 2
        return math.sqrt(sum_norm)

    @staticmethod
    def jacobi_method(A: Matrix, b: Matrix, optimum_residum):
        x_matrix = Matrix(b.size_x, b.size_y, 1)
        x_matrix_copy = Matrix(b.size_x, b.size_y, 1)
        k_iteration = 0
        N = A.size_x

        start = timeit.default_timer()
        while True:
            k_iteration += 1
            x_matrix_copy.fill_matrix(x_matrix)
            for i in range(x_matrix.size_y):
                x_sub = 0  # the value which we subtract from b_i
                for j in range(N):
                    if i == j:
                        continue
                    x_sub += A[i, j] * x_matrix_copy[j, 0]

                x_matrix[i, 0] = (b[i, 0] - x_sub) / A[i, i]
            # tu bedziemy sprawdzac norme z residum

            residum = np.subtract(np.dot(A.matrix_tab, x_matrix.matrix_tab), b.matrix_tab)

            norma_residum = MatrixResolver.__norm(residum)
            if norma_residum < optimum_residum:
                break
            if norma_residum > abs(10 ** (10)):
                raise OverflowError(f"Metoda Jacobiego nie zbiega się ")

        stop = timeit.default_timer()
        time = stop - start

        return x_matrix, k_iteration, norma_residum, time

    @staticmethod
    def gauss_seidel_method(A: Matrix, b: Matrix, optimum_residum):
        x_matrix = Matrix(b.size_x, b.size_y, 1)
        x_matrix_copy = Matrix(b.size_x, b.size_y, 1)
        k_iteration = 0
        N = A.size_x
        norma_residum = 0

        start = timeit.default_timer()
        while True:
            k_iteration += 1
            x_matrix_copy.fill_matrix(x_matrix)
            for i in range(x_matrix.size_y):
                x_sub = 0  # the value which we subtract from b_i
                for j in range(i):
                    if i == j:
                        continue
                    x_sub += A[i, j] * x_matrix[j, 0]
                for j in range(i + 1, N):
                    if i == j:
                        continue
                    x_sub += A[i, j] * x_matrix_copy[j, 0]
                x_matrix[i, 0] = (b[i, 0] - x_sub) / A[i, i]
            # tu bedziemy sprawdzac norme z residum

            residum = np.subtract(np.dot(A.matrix_tab, x_matrix.matrix_tab), b.matrix_tab)

            norma_residum = MatrixResolver.__norm(residum)

            if norma_residum < optimum_residum:
                break
            if norma_residum > abs(10 ** (10)):
                raise OverflowError(f"Metoda Gaussa-Seidel nie zbiega się ")

        stop = timeit.default_timer()
        time = stop - start

        return x_matrix, k_iteration, norma_residum, time

    @staticmethod
    def __make_LU(A: Matrix) -> (Matrix, Matrix):
        U = Matrix(A.size_x, A.size_y)
        U.fill_matrix(A)
        L = Matrix(A.size_x, A.size_y)
        L.fill_matrix_I()
        P = Matrix(A.size_x, A.size_y)
        P.fill_eye()

        m = A.size_x
        for x in range(m - 1):
            MatrixResolver.pivoting(L,U,P,x,m)
            for y in range(x + 1, m):
                L[y, x] = U[y, x] / U[x, x]
                for t in range(x, m):
                    U[y, t] -= L[y, x] * U[x, t]


        return L, U

    @staticmethod
    def pivoting(L:Matrix , U:Matrix  , P:Matrix, x , m):
        pivot = abs(U[x,x])
        pivot_index = x

        #find pivot
        for index in range(x , m):
            if pivot < abs(U[index , x]):
                pivot = abs(U[index , x])
                pivot_index = index
        if pivot_index == x:
            return

        for index in range(m):
            if index >= x:
                tmp = U[x,index]
                U[x,index] = U[pivot_index , index]
                U[pivot_index,index] = tmp
            else:
                tmp = L[x,index]
                L[x, index] = L[pivot_index, index]
                L[pivot_index, index] = tmp
            tmp = P[x, index]
            P[x,index] = P[pivot_index,index]
            P[pivot_index,index] = tmp





    @staticmethod
    def LU_method(A: Matrix, b: Matrix):
        start = timeit.default_timer()
        L , U = MatrixResolver.__make_LU(A)
        y_matrix = Matrix(b.size_x, b.size_y)
        x_matrix = Matrix(b.size_x, b.size_y)

        # calc Y matrix
        for y in range(y_matrix.size_y):
            x_subtract =0
            for x in range(y):
                x_subtract += L[y,x]*y_matrix[x,0]
            y_matrix[y,0] = b[y,0] - x_subtract
        # calc X matrix
        for y in range(y_matrix.size_y-1 , -1 , -1):
            x_subtract = 0
            for x in range(y+1,y_matrix.size_y):
                x_subtract += U[y, x] * x_matrix[x, 0]
            x_matrix[y, 0] = (y_matrix[y, 0] - x_subtract)/U[y,y]

        stop = timeit.default_timer()
        time = stop - start

        residum = np.subtract(np.dot(A.matrix_tab, x_matrix.matrix_tab), b.matrix_tab)

        norma_residum = MatrixResolver.__norm(residum)

        return x_matrix, norma_residum, time

    @staticmethod
    def display_results(k_iteration, norma_residum, time, method_string):
        print(method_string + " :")
        print("Time = " + str(time) + " Residum = " + str(norma_residum) + " Iterations = " + str(k_iteration))

    @staticmethod
    def display_results_LU(norma_residum, time):
        print("LU method :")
        print("Time = " + str(time) + " Residum = " + str(norma_residum) )
