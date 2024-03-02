class Singleton:
    pass


singleton_isntance_1 = Singleton()
print(f"{singleton_isntance_1=}")

singleton_isntance_2 = Singleton()
print(f"{singleton_isntance_2=}")

singleton_isntance_3 = Singleton()
print(f"{singleton_isntance_3=}")

# singleton_isntance_1 = <__main__.Singleton object at 0x0000029CF9957D60>
# singleton_isntance_2 = <__main__.Singleton object at 0x0000029CF9AB9CC0>
# singleton_isntance_3 = <__main__.Singleton object at 0x0000029CF9AB9D20>


class Car:
    __instance = None

    def __init__(self) -> None:
        if self.__instance is None:
            Car.__instance = self
        else:
            raise Exception("This class is Singleton.")

    @staticmethod
    def get_instance():
        if Car.__instance is None:
            Car()
        return Car.__instance


farari = Car()  # <__main__.Car object at 0x00000263E0D2B970>
print(f"{farari=}")

civic = Car.get_instance()  # <__main__.Car object at 0x00000263E0D2B970>
print(f"{civic=}")


bmw = Car()
# Raise Exception
