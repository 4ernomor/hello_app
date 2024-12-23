import unittest
import io
from unittest.mock import patch
from src.main import say_hello

class TestSayHello(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_say_hello_default(self, mock_stdout):
        say_hello()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, World!")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_say_hello_custom_name(self, mock_stdout):
        say_hello("TestUser")
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, TestUser!")

if __name__ == '__main__':
    unittest.main()
