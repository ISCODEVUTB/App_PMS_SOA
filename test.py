import unittest


def suma(a,b):
    return a+b


class BasicTest(unittest.TestCase):
    def test1(self):
        c = suma(5, 10)
        self.assertEqual(c, 15)



if __name__ == '_main_':
    unittest.main()
