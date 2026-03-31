from shape3d import Shape3D
import math

class Sphere(Shape3D):
    def __init__(self, colour, radius, x=0, y=0, z=0):
        super().__init__("Sphere", colour, x, y, z)
        self.__radius = radius

    def volume(self):
        return round((4 / 3) * math.pi * self.__radius ** 3, 2)

    def surface_area(self):
        return round(4 * math.pi * self.__radius ** 2, 2)

    def draw(self):
        print("      *******      ")
        print("    **       **    ")
        print("  **           **  ")
        print(" *               * ")
        print("*                 *")
        print("*                 *")
        print("*                 *")
        print(" *               * ")
        print("  **           **  ")
        print("    **       **    ")
        print("      *******      ")

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius