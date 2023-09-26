def add(*args):
    print(args[0])

    total = 0
    for n in args:
        total += n
    return total


# print(add(4, 12, 3, 4))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
