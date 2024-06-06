import discount_easy
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(discount_easy.dis(75, 25), 56.25)
    def test2(self):
        self.assertEqual()
    
if __name__ == '__main__':
    unittest.main()
