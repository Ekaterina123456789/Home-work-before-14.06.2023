from Home_work_14_06_2023_1 import NumberConverter
import unittest


class TestNumberConverter(unittest.TestCase):
    @unittest.skip
    def test_summa(self):
        self.assertEqual(24, NumberConverter.summa(8, 2, 10, 4))

    def test_average(self):
        self.assertEqual(6, NumberConverter.average(8, 2, 10, 4))

    def test_max(self):
        self.assertEqual(10, NumberConverter.max(8, 2, 10, 4))

    def test_min(self):
        self.assertEqual(2, NumberConverter.min(8, 2, 10, 4))


if __name__ == "__main__":
    unittest.main()
