import unittest

class Square(object):
    def __init__(self, Number) -> None:
        if type(Number) not in [int, float]:
            raise TypeError("Number must be int or float")
        
        if Number < 0:
            raise ValueError("Number must be positive")
        
        self.Number = Number
        
    def area(self):
        return self.Number * self.Number


# def setUpModule():
#     print("Running The UnitTest")
    
    
# def tearDownModule():
#     print("Ended the Unit Test")
    
    
class TestSquare(unittest.TestCase):
    def setUp(self) -> None:
        # print("Starting the Test")
        self.square = Square(100)
    
    def test_area(self):
        # square = Square(100)
        resultofarea = self.square.area()
        self.assertEqual(resultofarea, 10000)
        
    def test_area1(self):
        # square = Square(100)
        resultofarea = self.square.area()
        self.assertGreaterEqual(resultofarea,10000)
    
    @unittest.skip("W I P")   
    def test_with_wrong_type(self):
        with self.assertRaises(TypeError):
            Square(100)
    
    def tearDown(self) -> None:
        super().tearDown()
        self.square = None


@unittest.skip("NOt Implemented Yet")        
class Test_Demo(object):
    pass

if __name__ == '__main__':
    unittest.main()