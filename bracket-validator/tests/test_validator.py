import unittest

from bracket_validator import validate_brackets, format_result


class TestBracketValidator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(validate_brackets(""), (True, []))

    def test_valid_round_brackets(self):
        self.assertEqual(validate_brackets("(hello)"), (True, []))

    def test_valid_all_bracket_types(self):
        self.assertEqual(validate_brackets("<div>{(test)}</div>"), (True, []))

    def test_unclosed_opening_bracket(self):
        self.assertEqual(validate_brackets("(hello"), (False, [0]))

    def test_extra_closing_bracket(self):
        self.assertEqual(validate_brackets("hello)"), (False, [5]))

    def test_wrong_order(self):
        self.assertEqual(validate_brackets("({)}"), (False, [0, 1, 2, 3]))

    def test_format_valid_result(self):
        self.assertEqual(format_result("(ok)"), "Рядок валідний")

    def test_format_invalid_result_contains_positions(self):
        result = format_result("abc)")
        self.assertIn("abc)", result)
        self.assertIn("   ^", result)
        self.assertIn("позиціях: 3", result)


if __name__ == "__main__":
    unittest.main()
