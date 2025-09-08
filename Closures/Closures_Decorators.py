def called_counter_decorator(func) -> object:
    counter = 0
    def wrapper (*args, **kwargs):
        nonlocal counter
        counter += 1
        if counter <= 3:
            value = func(*args, **kwargs)
            return value
        else:
            print("You have already greeted three times")
    return wrapper

@called_counter_decorator
def greet_person(host: str, guest: str) -> str:
    return f"{host} welcomes {guest}"

if  __name__ == '__main__':
    print (greet_person("Gea", "Tatin"))
    print(greet_person("Gea", "Toby"))
    print(greet_person("Gea", "Roquefogoks"))
    print(greet_person("Gea", "Cabeza Huevo"))
