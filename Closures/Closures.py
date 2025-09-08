'''
   This is a simple script for playing with closure.
   It is meant for training and learning purposes
'''


def outer_function() -> object:
    record = []
    counter = 0

    def inner_function(*args, **kwargs):
        nonlocal counter
        counter = counter + 1
        print(*args, **kwargs)
        record.append(args)
        print(record)
        print(f"This is the number of times called: {counter}")

    return inner_function

if  __name__ == '__main__':
    inner_call = outer_function()
    inner_call("Hello from Gea")
    inner_call("Hello from Castores")
    inner_call("Hello from Tortugas", "Mini")
