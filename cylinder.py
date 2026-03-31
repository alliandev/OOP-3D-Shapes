from shape3d import Shape3D
import math

class Cylinder(Shape3D):
    def __init__(self, colour, radius, height, x=0, y=0, z=0):
        super().__init__("Cylinder", colour, x, y, z)
        self.__radius = radius
        self.__height = height

    def volume(self):
        return round(math.pi * self.__radius ** 2 * self.__height, 2)

    def surface_area(self):
        return round(2 * math.pi * self.__radius * (self.__radius + self.__height), 2)

    def draw(self):
        print("  ____  ")
        print(" /    \\ ")
        print("|      |")
        print("|      |")
        print(" \\____/ ")

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height

    def set_radius(self, radius):
        self.__radius = radius

    def set_height(self, height):
        self.__height = height