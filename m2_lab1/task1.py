# TODO Написать 3 класса с документацией и аннотацией типов

import doctest
from typing import Union


class Cube:
    def __init__(self, length: Union[float, int], color: str):
        """

        Создание и подготовка к работе объекта "Куб"

        :param length: Длина стороны куба
        :param color: Цвет куба

        Примеры:
        >>> cube = Cube(8, "красный")  # инициализация экземпляра класса
        """
        if not isinstance(length, (float, int)):
            raise TypeError('Длина стороны куба должна быть типа int или float')
        if not isinstance(color, str):
            raise TypeError('Цвет должен быть типа str')
        if length < 0:
            raise ValueError('Длина стороны куба должна быть больше нуля')
        self.length = length
        self.color = color

    def area(self) -> float:
        """
        Функция для вычисления площади поверхности куба

        :return: Площадь поверхности куба

        Примеры:
        >>> cube = Cube(8, "красный")
        >>> print(cube.area())
        384.0
        """
        s = 6 * self.length ** 2
        return s

    def volume(self) -> float:
        """
        Функция для вычисления объема куба

        :return: Объем куба

        Примеры:
        >>> cube = Cube(8, "красный")
        >>> print(cube.volume())
        512.0
        """
        v = self.length ** 3
        return v


class Cat:
    def __init__(self, name: str, age: int, breed: str):
        """
        Создание и подготовка к работе объекта "Кот"

        :param name: Имя кота
        :param age: Возраст кота
        :param breed: Порода кота

        Примеры:
        >>> cat = Cat("Ричард", 9, "шотландский прямоухий")
        """
        if not isinstance(name, str):
            raise TypeError("Имя кота должно быть строкой")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст кота должен быть положительным числом")
        if not isinstance(breed, str):
            raise TypeError("Порода кота должна быть строкой")
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self) -> str:
        """
        Кот издает звук "мяу".

        :return: Строка "мяу"

        Примеры:
        >>> cat = Cat("Ричард", 9, "шотландский прямоухий")
        >>> cat.meow()
        'мяу'
        """
        return "мяу"

    def eat(self, food: str) -> None:
        """
        Кот ест определенную еду.

        :param food: Тип еды

        Примеры:
        >>> cat = Cat("Ричард", 9, "шотландский прямоухий")
        >>> cat.eat("сухой корм")
        """
        ...


class House:
    def __init__(self, address: str, area: float, floors: int):
        """
        Создание и подготовка к работе объекта "Дом"

        :param address: Адрес дома
        :param area: Площадь дома в квадратных метрах
        :param floors: Количество этажей

        Примеры:
        >>> house = House("ул. Садовая, 11", 100.0, 1)
        """
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть строкой")
        if not isinstance(area, (int, float)) or area <= 0:
            raise ValueError("Площадь дома должна быть положительным числом")
        if not isinstance(floors, int) or floors <= 0:
            raise ValueError("Количество этажей должно быть положительным числом")
        self.address = address
        self.area = area
        self.floors = floors

    def open_door(self) -> None:
        """
        Открытие двери дома

        Примеры:
        >>> house = House("ул. Садовая, 11", 100.0, 1)
        >>> house.open_door()
        """
        ...

    def lease(self) -> None:
        """
        Сдача дома в аренду

        Примеры:
        >>> house = House("ул. Садовая, 11", 100.0, 1)
        >>> house.lease()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()