import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42),42, "should be number")
        print("yes")
    def test_abs2(self):
        self.assertEqual(abs(-42),-42, "should be number")
        print("no")
    def test_abs3(self):
        self.assertEqual(abs(-42),42, "should be number")
        print("yes2")
        

if __name__ == "__main__":
    unittest.main()
