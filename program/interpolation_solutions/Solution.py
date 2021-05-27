
from program.objects.Area import Area

import matplotlib.pyplot as plt

from program.utils.path import determine_directory
from program.utils.path import determine_absolute_path


class Solution:

    def __init__(self , area:Area ,amount_of_markers ,even  ):
        self.area = area
        self.amount_of_markers = amount_of_markers
        self.even = even
        if even:
            self.selected_points = self.__select_points_even(amount_of_markers)
        else:
            self.selected_points = self.__select_points_not_even(amount_of_markers)
        self.points_interpolation = list()

    def show_plots(self):
        plt.title(f"{self} = {self.area.name} dla {self.amount_of_markers} markerów")
        x_array_normal = [point.x for point in self.area.points]
        y_array_normal = [point.y for point in self.area.points]
        x_array_interpolation = [point.x for point in self.points_interpolation]
        y_array_interpolation = [point.y for point in self.points_interpolation]
        x_selected_points = [point.x for point in self.selected_points]
        y_selected_points = [point.y for point in self.selected_points]

        plt.plot(x_array_normal,y_array_normal ,color="blue" , label="normal")
        plt.plot(x_array_interpolation,y_array_interpolation, color="orange" , label="interpolation")
        plt.scatter(x_selected_points , y_selected_points ,marker="o" , color="red")
        plt.xlabel("Dystans")
        plt.ylabel("Wysokość")
        plt.legend()

        is_even_string = f"_selected" if not self.even else f""
        plt.savefig(determine_absolute_path(determine_directory("charts"),f"{self}_{self.area.name}_{self.amount_of_markers}m{is_even_string}"))

    def __select_points_even(self, amount_of_markers) -> list:
        offset = int(len(self.area.points) / (amount_of_markers - 1))
        list_of_points = [self.area.points[index] for index in range(0, len(self.area.points), offset)]
        list_of_points.pop()
        list_of_points.append(self.area.points[-1])
        return list_of_points

    def __select_points_not_even(self , amount_of_markers):
        list_of_points = list()
        if amount_of_markers == 14:
            offset = int((len(self.area.points)-40) / (amount_of_markers -6))
            list_of_points.append(self.area.points[0])
            list_of_points.append(self.area.points[9])
            list_of_points.append(self.area.points[18])
            for index in range(offset+18 , len(self.area.points) , offset):
                list_of_points.append(self.area.points[index])
            list_of_points.append(self.area.points[len(self.area.points)-20])
            list_of_points.append(self.area.points[len(self.area.points)-10])
            list_of_points.append(self.area.points[len(self.area.points)-1])
        if amount_of_markers == 10:
            offset = int((len(self.area.points)-60) / (amount_of_markers -4))
            list_of_points.append(self.area.points[0])
            list_of_points.append(self.area.points[30])
            for index in range(offset+30 , len(self.area.points) , offset):
                list_of_points.append(self.area.points[index])
            list_of_points.append(self.area.points[len(self.area.points)-30])
            list_of_points.append(self.area.points[len(self.area.points)-1])

        return list_of_points
