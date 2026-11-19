import unittest
from unittest.mock import mock_open, patch

from lab4 import calculate_traffic


class TestCalculateTraffic(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data=
           '127.0.0.1 - - [07/May/2017:10:00:00 +0300] "GET / HTTP/1.0" 200 100 "-" "Browser"\n'
           '127.0.0.1 - - [07/May/2017:10:00:01 +0300] "POST /login HTTP/1.0" 200 250 "-" "Browser"\n')
    def test_two_log_records(self, mock_file):
        sent, received = calculate_traffic("test.log")

        self.assertEqual(sent, 350)
        self.assertEqual(received, len("GET / HTTP/1.0") + len("POST /login HTTP/1.0"))
        mock_file.assert_called_once_with("test.log", "r", encoding="utf-8-sig")

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_empty_file(self, mock_file):
        sent, received = calculate_traffic("empty.log")

        self.assertEqual(sent, 0)
        self.assertEqual(received, 0)

    @patch("builtins.open", new_callable=mock_open, read_data=
           'this line is not an nginx log\n'
           '127.0.0.1 - - [07/May/2017:10:00:00 +0300] "GET /page HTTP/1.0" 200 42 "-" "Browser"\n')
    def test_invalid_line_is_skipped(self, mock_file):
        sent, received = calculate_traffic("mixed.log")

        self.assertEqual(sent, 42)
        self.assertEqual(received, len("GET /page HTTP/1.0"))


if __name__ == "__main__":
    unittest.main()
