class RootCalculator:
    def __init__(self, root_degree : int) -> None:
        self.root_degree = root_degree

    def __call__(self, number : int) -> int:
        return pow(number, 1 / self.root_degree)


if __name__ == '__main__':

    square_root = RootCalculator(2)
    print(square_root(49))

    cube_root = RootCalculator(3)
    print(cube_root(125))



