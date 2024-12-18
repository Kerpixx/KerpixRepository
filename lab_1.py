# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Glass:
    """
        Документация на класс.
        Класс описывает модель стакана.
    """

    def __init__(self, height: float, bottom_radius: float):
        """
         Создание и подготовка к работе объекта Стакан.
         :param height: высота стакана
         :param bottom_radius: радиус дня стакана
         Примеры:
         >>> glass = Glass(50.0, 10.0)  # инициализация экземпляра класса
         """

        if not isinstance(height, float):
            raise TypeError("Высота стакана должна быть типа float")
        if height <= 0:
            raise ValueError("Высота стакана должна быть положительным числом")
        self.height = height

        if not isinstance(bottom_radius, float):
            raise TypeError("Радиус дна должен быть float")
        if bottom_radius <= 0:
            raise ValueError("Радиус дна должен быть положительным числом")
        self.bottom_radius = bottom_radius

    def count_volume(self):
        """
                Функция которая позволяет вычислить объем стакана
                :return: Объем стакана
                Примеры:
                >>> glass = Glass(30.0, 10.0)
                >>> glass.count_volume()
        """
        ...

    def count_another_height(self, new_bottom_radius: float) -> float:
        """
            Функция, которая позволяет вычислить новую высоту стакана для заданного радиуса, и такого же объема,
            как имеющийся стакан
            :return: Объем стакана
            Примеры:
            >>> glass = Glass(30.0, 10.0)
            >>> glass.count_another_height(15.0)
        """
        if new_bottom_radius <= 0:
            raise ValueError("Радиус стакана должна быть положительным числом")
        ...

class Cube:
    """
        Документация на класс.
        Класс описывает модель стакана.
    """

    def __init__(self, edge: float, water: float):
        """
         Создание и подготовка к работе объекта Куб.
         :param edge: рубро куба
         :param water: количество воды внутри
         Примеры:
         >>> cube = Cube(50.0,10.0)  # инициализация экземпляра класса
         """

        if not isinstance(edge, float):
            raise TypeError("Ребро куба должно быть типа float")
        if edge <= 0:
            raise ValueError("Ребро куба должно быть быть положительным числом")
        self.edge = edge

        if not isinstance(water, float):
            raise TypeError("Объем воды внутри должно быть типа float")
        if water <= 0:
            raise ValueError("Объем воды внутри быть быть положительным числом")
        self.water = water

    def count_volume(self) -> float:
        """
                Функция которая позволяет вычислить объем куба
                :return: Объем стакана
                Примеры:
                >>> cube = Cube(30.0, 10.0)
                >>> cube.count_volume()
        """
        ...

    def is_empty_cube(self) -> bool:
        """
        Функция которая проверяет является ли куб пустым
        :return: Является ли куб пустым
        Примеры:
        >>> cube = Cube(30.0, 10.0)
        >>> cube.is_empty_cube()
        """
        ...

class House:
    """
        Документация на класс.
        Класс описывает модель дома.
    """

    def __init__(self, floor: int, occupied_apartments: int):
        """
         Создание и подготовка к работе объекта Куб.
         :param floor: количество этажей в доме
         :param occupied_apartments: количество занятых квартир в доме
         Примеры:
         >>> house = House(20,20)  # инициализация экземпляра класса
         """

        if not isinstance(floor, int):
            raise TypeError("Количество этажей в доме должно быть типа int")
        if floor <= 0:
            raise ValueError("Количество этажей в доме должно быть быть положительным числом")
        self.floor = floor

        if not isinstance(occupied_apartments, int):
            raise TypeError("количество занятых квартир в доме  должно быть типа int")
        if occupied_apartments <= 0:
            raise ValueError("количество занятых квартир в доме должно быть быть положительным числом")
        self.occupied_apartments = occupied_apartments

    def count_volume(self) -> int:
        """
                Функция которая позволяет вычислить количество квартир в доме
                :return: Количество квартир в доме
                Примеры:
                >>> house = House(20,20)
                >>> house.count_volume()
        """
        ...

    def is_empty_house(self) -> bool:
        """
        Функция которая проверяет есть ли в доме свободный квартиры
        :return: Является ли дом полностью заселённым пустым
        Примеры:
        >>> house = House(20,20)
        >>> house.is_empty_house()
        """
        ...




if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()
