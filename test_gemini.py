import unittest
import io
import sys
from unittest.mock import patch
import gemini  # Assuming gemini.py is in the same directory


class TestGemini(unittest.TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_output(self, mock_stdout):
        """Tests that the main function prints the expected output, including the loop."""
        gemini.main()  # Run the main function
        expected_output = "Hello from gemini.py!\nThis is iteration number: 1\nThis is iteration number: 2\nThis is iteration number: 3\nThis is iteration number: 4\nThis is iteration number: 5\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
