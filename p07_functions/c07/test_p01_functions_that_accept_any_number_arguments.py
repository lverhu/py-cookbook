import unittest
from p01_functions_that_accept_any_number_arguments import avg, make_element

class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
    def testAvg(self):
        self.assertEqual(2.0, avg(1, 2, 3))

    def test_make_element(self):
        element = make_element('item', 'Albatross', size='large', quantity=6)
        self.assertEqual("<item size=large quantity=6>Albatross</item>", element)


if __name__ == '__main__':
    unittest.main()