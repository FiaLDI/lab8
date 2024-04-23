import unittest
import primer_calc


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(primer_calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(primer_calc.sub(4, 2), 2)

    def test_mul(self):
        self.assertEqual(primer_calc.mul(2, 5), 40)

    def test_div(self):
        self.assertEqual(primer_calc.div(8, 4), 2)


if __name__ == "__main__":
    unittest.main()