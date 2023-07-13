import unittest as ut

from leetcode.binary_operation import set_0, set_1, set_digit


class TestBinaryOperation(ut.TestCase):
    def setUp(self) -> None:
        self.input_1 = 0b0001;
        self.input_2 = 0b0100;

    def test_set_0(self):
        result_1 = set_0(self.input_1, 0)
        self.assertEqual(result_1, 0b0000)

        result_2 = set_0(self.input_2, 1)
        self.assertEqual(result_2, 0b0100)

        result_3 = set_0(self.input_2, 2)
        self.assertEqual(result_3, 0b0000)

    def test_set_1(self):
        result_1 = set_1(self.input_1, 0)
        self.assertEqual(result_1, 0b0001)

        result_2 = set_1(self.input_2, 1)
        self.assertEqual(result_2, 0b0110)

        result_3 = set_1(self.input_2, 2)
        self.assertEqual(result_3, 0b0100)

    def test_set_digit(self):
        result = set_digit(self.input_1, 0, 0)
        self.assertEqual(result, 0b0000)
        result = set_digit(self.input_1, 1, 0)
        self.assertEqual(result, 0b0001)

        result = set_digit(self.input_1, 0, 1)
        self.assertEqual(result, 0b0001)
        result = set_digit(self.input_1, 1, 1)
        self.assertEqual(result, 0b0011)

        result = set_digit(self.input_2, 0, 0)
        self.assertEqual(result, 0b0100)
        result = set_digit(self.input_2, 1, 0)
        self.assertEqual(result, 0b0101)

        result = set_digit(self.input_2, 0, 2)
        self.assertEqual(result, 0b0000)
        result = set_digit(self.input_2, 1, 2)
        self.assertEqual(result, 0b0100)
