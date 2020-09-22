class Dog:
    def __init__(self) -> None:
        self.name = "Dog"

    @staticmethod
    def bark() -> str:
        return "woof!"


class Cat:
    def __init__(self) -> None:
        self.name = "Cat"

    @staticmethod
    def meow() -> str:
        return "meow!"


class Human:
    def __init__(self) -> None:
        self.name = "Human"

    @staticmethod
    def speak() -> str:
        return "'hello'"


class Car:
    def __init__(self) -> None:
        self.name = "Car"

    @staticmethod
    def make_noise(octane_level: int) -> str:
        return f"vroom{'!' * octane_level}"


class Adapter:

    def __init__(self, obj, **methods):
        self.obj = obj
        self._dict = methods

    def __getattr__(self, item):
        if item in self._dict:
            return self._dict[item]
        return getattr(self.obj, item)

    def origin_dict(self):
        return self._dict


if __name__ == '__main__':
    c = Car()
    c.make_noise(10)
    h = Human()
    s = Adapter(h, make_noise=h.speak).make_noise()
    print(s)
