from abc import ABC, abstractmethod

class Figures(ABC):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def figure_name(self):
        pass

    @abstractmethod
    def figure_size(self):
        pass

    def whatFigure(self):
        print(f"Figure: {self.figure_name()}")

    def whatSize(self):
        print(f"Size: {self.figure_size()} cm2\n")

class Triangle(Figures):

    def figure_name(self):
        return "Triangle"

    def figure_size(self):
        return (self.x*self.y)/2

class Square(Figures):

    def figure_name(self):
        return "Square"

    def figure_size(self):
        return self.x * self.y

class Cuboid(Figures):

    def figure_name(self):
        return "Cuboid"

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def figure_size(self):
        return self.x * self.y * self.z

def main():
    Trojkat = Triangle(4, 5)
    Kwadrat = Square(3,6)
    Prostopadloscian = Cuboid(7, 6, 8)

    Trojkat.whatFigure()
    Trojkat.whatSize()

    Kwadrat.whatFigure()
    Kwadrat.whatSize()

    Prostopadloscian.whatFigure()
    Prostopadloscian.whatSize()

if __name__ == "__main__":
    print()
    main()
