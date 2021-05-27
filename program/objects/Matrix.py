import math
from copy import deepcopy


class Matrix:

    def __init__(self,size_x , size_y,value=0):
        self.size_x = size_x
        self.size_y = size_y
        self.matrix_tab = [[value for x in range(size_x)] for y in range(size_y)]
    def __getitem__(self, position):
        y,x = position
        if y < 0 or y >= self.size_y:
            raise IndexError("y is out of range")
        if x < 0 or x >= self.size_x:
            raise IndexError("x is out of range")
        return self.matrix_tab[y][x]
    def __setitem__(self, position, value):
        y, x = position
        if y < 0 or y >= self.size_y:
            raise IndexError("y is out of range")
        if x < 0 or x >= self.size_y:
            raise IndexError("x is out of range")
        self.matrix_tab[y][x] = value


    def display(self):
        for y in range(self.size_y):
            print(self.matrix_tab[y])

    def fill_matrix_A(self ,a1,a2,a3):
        pattern = [a3,a2,a1,a2,a3]
        offset_global = -2
        for y in range(self.size_y):
            current_offset = offset_global
            for patter_x in range(len(pattern)):
                if current_offset < 0 or current_offset > self.size_x -1:
                    current_offset += 1
                    continue
                self.matrix_tab[y][current_offset] = pattern[patter_x]
                current_offset += 1
            offset_global += 1

    def fill_matrix_b(self,tab):
        for y in range(self.size_y):
            self.matrix_tab[y][0] = tab[y]
    def fill_eye(self ):
        for y in range(self.size_y):
            for x in range(self.size_x):
                if y == x:
                    self.matrix_tab[y][x] = 1


    def fill_matrix_I(self):
        for i in range(self.size_y):
            self.matrix_tab[i][i] = 1
    def fill_row(self ,index ,row):
        for x in range(self.size_x):
            self.matrix_tab[index][x] = row[x]

    def fill_matrix(self , other_matrix):
        self.matrix_tab = deepcopy(other_matrix.matrix_tab)



