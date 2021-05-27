from program.interpolation_solutions.Solution import Solution
from program.objects.Matrix import Matrix
from program.objects.MatrixResolver import MatrixResolver
from program.objects.Point import Point
from numpy import *


class Spline(Solution):

    def __init__(self, area, amount_of_markers, even):
        super().__init__(area, amount_of_markers, even)

    def __str__(self):
        return f"Spline"

    def create_splines(self, current_x):
        N = 4 * (len(self.selected_points) - 1)
        n = len(self.selected_points)
        A = Matrix(N, N)
        b = [0.0 for i in range(N)]

        for index in range(n - 1):
            if index == 0:
                h = self.selected_points[1].x - self.selected_points[0].x
            else:
                h = self.selected_points[index].x - self.selected_points[index - 1].x

            A[4 * index, 4 * index] = 1

            b[4 * index] = self.selected_points[index].y

            A[4 * index + 1, 4 * index] = 1
            A[4 * index + 1, 4 * index + 1] = h
            A[4 * index + 1, 4 * index + 2] = h ** 2
            A[4 * index + 1, 4 * index + 3] = h ** 3
            b[4 * index + 1] = self.selected_points[index + 1].y
            if index == 0:
                A[2, 2] = 1
                b[2] = 0

                h = self.selected_points[n - 1].x - self.selected_points[n - 2].x
                A[3, 4 * (n - 2) + 2] = 2
                A[3, 4 * (n - 2) + 3] = 6 * h
                b[3] = 0
            else:
                A[4 * index + 2, 4 * (index - 1) + 1] = 1
                A[4 * index + 2, 4 * (index - 1) + 2] = 2 * h
                A[4 * index + 2, 4 * (index - 1) + 3] = 3 * h * h
                A[4 * index + 2, 4 * index + 1] = -1
                b[4 * index + 2] = 0

                A[4 * index + 3, 4 * (index - 1) + 2] = 2
                A[4 * index + 3, 4 * (index - 1) + 3] = 6 * h
                A[4 * index + 3, 4 * index + 2] = -2
                b[4 * index + 3] = 0

        matrix_b = Matrix(1, N)
        matrix_b.fill_matrix_b(b)
        result, norma_residum, time = MatrixResolver.LU_method(A, matrix_b)

        current_y = 0
        for index in range(n - 1):
            current_y = 0.0
            if self.selected_points[index].x <= current_x <= self.selected_points[index+1].x:
                for j in range(4):
                    h = current_x - self.selected_points[index].x

                    current_y += result[4 * index + j, 0] * (h ** j)
                break

        return Point(current_x, current_y)

    def create(self):
        if len(self.selected_points) == 0:
            raise NotImplementedError("selected points are not choosen ")
        offset = int((self.area.points[-1].x)/160)
        for x in range(0, int(self.area.points[len(self.area.points) - 1].x) + 1, offset):
            self.points_interpolation.append(self.create_splines(x))
