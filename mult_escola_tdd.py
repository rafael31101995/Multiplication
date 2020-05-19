import unittest
import mult_escola_rafael as school


class Test_multiplication(unittest.TestCase):
    def setUp(self):
        pass

    def test_multiplication(self):
        self.assertEqual(school.multiplication('999999999999999', '8888888888888'), '8888888888887991111111111112')
        self.assertEqual(school.multiplication('999999999999999', '0'), '0')
        self.assertEqual(school.multiplication('-1', '1'), '-1')
        self.assertEqual(school.multiplication('-1', '-1'), '1')
        self.assertEqual(school.multiplication('100', '2000'), '200000')