class Car:
    def __init__(self, make:str, model:str, year:int, color:str):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    def accelerate(self, value:int) -> None:
        if not self.started:
            print("Car is not started!")
            return
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            self.speed = self.max_speed
        print(f"Accelerating to {self.speed} km/h...")

    def brake(self, value) -> None:
        if self.speed - value >= 0:
            self.speed -= value
        else:
            self.speed = 0
        print(f"Braking to {self.speed} km/h...")

    def __str__(self):
        return f"{self.make} {self.model}, {self.color} ({self.year})"

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f'(make="{self.make}", '
            f'model="{self.model}", '
            f"year={self.year}, "
            f'color="{self.color}")'
        )
class ThreeDPoint:
     def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
     def __iter__(self):
        yield from (self.x, self.y, self.z)
