
from program.interpolation_solutions.Solution import Solution

from program.objects.Point import Point

class Langrange(Solution):

    def __init__(self ,area ,amount_of_markers ,even):
        super().__init__(area,amount_of_markers ,even )

    def create(self):
        if len(self.selected_points) == 0:
            raise NotImplementedError("selected points are not choosen ")
        for x in range(int(self.area.points[len(self.area.points)-1].x)+1):
            self.points_interpolation.append(self.determine_point(x))

    def determine_point(self , x ):
        y_of_x = 0.0
        for i in range(len(self.selected_points)):
            piece_result= self.selected_points[i].y
            for j in range(len(self.selected_points)):
                if i != j :
                    piece_result *= ((x - self.selected_points[j].x) / (
                            self.selected_points[i].x - self.selected_points[j].x))
            y_of_x += piece_result
        return Point(x , y_of_x)

    def __str__(self):
        return f"Langrange"