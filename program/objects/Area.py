from _csv import reader

from program.utils.path import determine_absolute_path
from program.utils.path import determine_directory

from program.objects.Point import Point



class Area:

    datagram_directory = determine_directory("dataset")

    def __init__(self , name:str):
        self.points = list()
        self.name = name
        self.__load_data_set()
    def __check_row(self, row):
        for elem in row:
            if elem is None:
                return False
        return True

    def __load_data_set(self):
        path = determine_absolute_path(Area.datagram_directory,f"{self.name}.csv")
        with open(path) as file_to_read:
            csv_reader = list(reader(file_to_read))
            k = 0
            for row in csv_reader[1:]:
                if not len(row): continue
                if not self.__check_row(row):
                    raise ValueError("Some values in row can be null")
                self.points.append(Point(row))
                k +=1
            print(k)
