
class Point:

    @staticmethod
    def __valid_cord(stringFloat):
        if not isinstance(stringFloat, str):
            raise TypeError("Error in valid_float value is not string")
        return float(stringFloat.replace(",", ""))

    def __init__(self ,*args):
        if isinstance(args[0],list):
            self.x = Point.__valid_cord(args[0][0])
            self.y = Point.__valid_cord(args[0][1])
        else:
            self.x = args[0]
            self.y = args[1]


    def __str__(self):
        return f"Point(x={self.x} , y ={self.y})"