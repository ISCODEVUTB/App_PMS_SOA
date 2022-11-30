import unittest
import app

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(app.suma(1,2), 3)
    
    def test(self):
        self.assertEqual(app.connect(), "connected")

if __name__ == '__main__':
    unittest.main()