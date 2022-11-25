import unittest


def suma(a,b):
    return a+b


class BasicTest(unittest.TestCase):
    def test1(self):
        c = suma(5, 10)
        self.assertEqual(c, 15)


<<<<<<< HEAD
if __name__ == '_main_':
=======
if __name__ == 'main':
>>>>>>> 6d7eac1b75fa2862abc9a95ba0071ba11da54862
    unittest.main()
