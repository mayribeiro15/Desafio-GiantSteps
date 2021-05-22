import unittest
from bolsaGotham import validate_line

class Tests(unittest.TestCase):
    def test_validation(self):
        self.assertEqual(validate_line('ACEC4', 'SELL', '10'), [0,0,0,0,0])
        self.assertEqual(validate_line('ACEC41', 'BUY', '100'), [0,0,0,0,0])
        self.assertEqual(validate_line('ACEC', 'SELL', '10'), [0,0,0,0,1])
        self.assertEqual(validate_line('ACEC4', 'SELL', '11'), [0,0,1,0,0])
        self.assertEqual(validate_line('ACEC44', 'SELL', '0'), [0,1,0,0,0])
        self.assertEqual(validate_line('ACEC', 'BUY', '10'), [0,0,0,0,1])

if __name__ == '__name__':
    unittest.main()