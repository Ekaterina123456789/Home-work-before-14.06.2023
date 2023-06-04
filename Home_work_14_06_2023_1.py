# Задание 1
# Создайте класс, содержащий набор целых чисел.
# В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

class NumberConverter:
    @staticmethod
    def summa(*args):
        return sum(args)

    @staticmethod
    def average(*args):
        return sum(args) / len(args)

    @staticmethod
    def max(*args):
        return max(*args)

    @staticmethod
    def min(*args):
        return min(*args)
