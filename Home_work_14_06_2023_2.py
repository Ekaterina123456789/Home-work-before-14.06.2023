# Задание 2 Сначала я нашла встроенные методы для перевода чисел в другие системы исчисления(oct, hex, bin),
# но потом решила немного усложнить задачу и прописать формулы для перевода.
# Это самая быстро сделанная домашка за последнее время!
# А то я уже хотела бросить учебу, т.к. с классами дз идёт сложновато.

# Создайте класс для числа. В классе должна быть реализована следующая функциональность:
# ■ Запись и чтение значения.
# ■ Перевод числа в восьмеричную систему исчисления.
# ■ Перевод числа в шестнадцатеричную систему исчисления.
# ■ Перевод числа в двоичную систему исчисления.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

class NumberConverter:
    @staticmethod
    def write_num():
        num = int(input('Введите число: '))
        return num

    @staticmethod
    def get_num():
        num = NumberConverter.write_num()
        return num

    @staticmethod
    def converter8(num):
        # num = NumberConverter.get_num() - хотела для получения числа ссылаться на get_num, но так неудобно тестировать
        num1 = num
        res = []
        while num > 0:
            remainder = num % 8
            res.append(remainder)
            num = num // 8
        print(f'Перевод в восьмеричную систему\n {num1} =')
        return int("".join(map(str, res[::-1])))

    @staticmethod
    def converter16(num):
        # num = NumberConverter.get_num()
        num1 = num
        res = []
        while num > 0:
            remainder = num % 16
            if remainder == 10:
                remainder = 'A'
            elif remainder == 11:
                remainder = 'B'
            elif remainder == 12:
                remainder = 'C'
            elif remainder == 13:
                remainder = 'D'
            elif remainder == 14:
                remainder = 'E'
            elif remainder == 15:
                remainder = 'F'
            res.append(remainder)
            num = num // 16
        print(f'Перевод в шестнадцатеричную систему\n {num1} =')
        return "".join(map(str, res[::-1]))

    @staticmethod
    def converter2(num):
        # num = NumberConverter.get_num()
        num1 = num
        res = []
        while num > 0:
            remainder = num % 2
            res.append(remainder)
            num = num // 2
        print(f'Перевод в двоичную систему\n {num1} =')
        return int("".join(map(str, res[::-1])))


print(NumberConverter.converter8(456))
print(NumberConverter.converter16(456))
print(NumberConverter.converter2(456))
