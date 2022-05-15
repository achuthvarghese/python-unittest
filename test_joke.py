import unittest
from unittest.mock import MagicMock, patch

from joke import get_joke, len_joke


class TestJoke(unittest.TestCase):
    @patch("main.get_joke")
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "some random joke"

        self.assertEqual(len_joke(), 16)

    @patch("main.requests")
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=200)
        mock_response.json.return_value = {"value": {"joke": "some other random joke"}}

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "some other random joke")

    @patch("main.requests")
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=403)

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "No jokes")


if __name__ == "__main__":
    unittest.main()