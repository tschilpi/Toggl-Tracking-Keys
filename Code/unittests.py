import unittest
from unittest.mock import Mock, patch
import main_test
import json
import requests

# mocktests
class TestFetchUserData(unittest.TestCase):

    @patch('main_test.requests.get')
    def test_valid_api_key(self, mock_get):
        # Mock the response for a valid API key
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = json.loads('[{"id": 1, "name": "Project 1"}, {"id": 2, "name": "Project 2"}]')

        api_key = "valid_api_key"
        result = main_test.fetch_user_data()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

    @patch('main_test.requests.get')
    def test_invalid_api_key(self, mock_get):
        # Mock the response for an invalid API key
        mock_get.return_value = Mock(status_code=403)

        api_key = "invalid_api_key"
        result = main_test.fetch_user_data()

        self.assertIsNone(result)

    @patch('main_test.requests.get')
    def test_network_error(self, mock_get):
        # Simulate a network error
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        api_key = "some_api_key"
        with self.assertRaises(requests.exceptions.RequestException):
            main_test.fetch_user_data()

if __name__ == '__main__':
    unittest.main()