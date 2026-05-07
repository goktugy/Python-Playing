from Descriptor_Square_Circle import Circle, Square
from Properties_Triangle import Triangle


if __name__ == "__main__":
    circle = Circle(5)
    print(f"Circle area is {circle.calculate_area()}")
    circle.radius=6
    print(f"Circle new radius is {circle.radius}")
    print(f"Circle new area is {circle.calculate_area()}")

    square = Square(10)
    print(f"Square area is {square.calculate_area()}")
    square.side=12
    print(f"Square new side is {square.side}")
    print(f"Square new area is {square.calculate_area()}")

    triangle = Triangle(6, 4)
    print(f"Triangle area is {triangle.calculate_area()}")

    triangle.base=10
    triangle.height=12
    print(f"Triangle new area is {triangle.calculate_area()}")



