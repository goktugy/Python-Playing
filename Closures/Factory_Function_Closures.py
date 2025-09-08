def make_root_calculator(root_degree) -> object:
    def root_calculator(number):
        return pow(number, (1/root_degree))
    return root_calculator

if  __name__ == '__main__':
    square_root = make_root_calculator(2)
    print(square_root(49))
    cube_root = make_root_calculator(3)
    print(cube_root(125))
