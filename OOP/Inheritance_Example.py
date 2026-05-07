class Aircraft:
    def __init__(self, thrust:int, lift:int, max_speed:int):
        self.thrust = thrust
        self.lift = lift
        self.max_speed = max_speed

    def show_technical_specs(self):
        print(f"Thrust: {self.thrust} kW")
        print(f"Lift: {self.lift} kg")
        print(f"Max speed: {self.max_speed} km/h")

    def fly (self) -> None:
        print(f"Flying at {self.thrust} km/h")


class Helicopter(Aircraft):
    def __init__(self, thrust:int, lift:int, max_speed:int, num_rotors:int):
        super().__init__(thrust, lift, max_speed)
        self.num_rotors = num_rotors

    def show_technical_specs(self):
        super().show_technical_specs()
        print(f"Number of rotors: {self.num_rotors}")

    def fly (self) -> None:
        print(f"Flying with {self.num_rotors} rotors ")