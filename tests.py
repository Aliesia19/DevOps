import unittest
from contextlib import redirect_stdout
from io import StringIO

from string_utils import print_string, check_case
from generators import parity_generator


class TestStringFunctions(unittest.TestCase):

    def capture_output(self, function, *args):
        output = StringIO()

        with redirect_stdout(output):
            function(*args)

        return output.getvalue().strip()

    def test_print_string(self):
        result = self.capture_output(print_string, "Hello")
        self.assertEqual(result, "Hello")

    def test_print_string_invalid_type(self):
        result = self.capture_output(print_string, 123)
        self.assertIn("Помилка", result)

    def test_check_case_uppercase(self):
        result = self.capture_output(check_case, "HELLO")
        self.assertIn("великі", result.lower())

    def test_check_case_lowercase(self):
        result = self.capture_output(check_case, "hello")
        self.assertIn("малі", result.lower())

    def test_check_case_mixed(self):
        result = self.capture_output(check_case, "Hello")
        self.assertIn("змішаний", result.lower())

    def test_check_case_empty_string(self):
        result = self.capture_output(check_case, "")
        self.assertIn("порожній", result.lower())

    def test_check_case_invalid_type(self):
        result = self.capture_output(check_case, 123)
        self.assertIn("Помилка", result)

    def test_parity_generator(self):
        generator = parity_generator()

        result = [next(generator) for _ in range(4)]

        self.assertEqual(
            result,
            ["Парне", "Непарне", "Парне", "Непарне"]
        )


if __name__ == "__main__":
    unittest.main()