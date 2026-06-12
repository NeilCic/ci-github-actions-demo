import unittest
from main import test

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(test(), "test me")

if __name__ == "__main__":
    unittest.main()
