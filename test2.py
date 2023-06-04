from Home_work_14_06_2023_2 import NumberConverter
import unittest


class TestNumberConverter(unittest.TestCase):
    def test_get_number(self):
        self.assertEqual(456, NumberConverter.get_num())

    def test_converter8(self):
        self.assertEqual(710, NumberConverter.converter8(456))

    def test_converter16(self):
        self.assertEqual('1C8', NumberConverter.converter16(456))

    def test_converter2(self):
        self.assertEqual(111001000, NumberConverter.converter2(456))


if __name__ == "__main__":
    unittest.main()
