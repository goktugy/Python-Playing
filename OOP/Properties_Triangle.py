class Triangle:
    def __init__(self, height:int | float, base:int | float):
        self._height = height
        self._base = base

    @property
    def height(self) ->int:
        return self._height

    @height.setter
    def height(self, value:int | float):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        self._height = value

    @property
    def base(self) -> int:
        return self._base

    @base.setter
    def base(self, value:int | float):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        self._height = value

    def calculate_area(self) -> int | float:
        return  (self._base * self._height)/2