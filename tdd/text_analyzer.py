import unittest
import os


def analyze_text(filename):
    """Calculate the number of lines and characters in a file.

    Args:
        filename: The name of the file to analyze.

    Raises:
        IOError: If ``filename`` does not exist or can't be read.

    Returns: A tuple where the first element is the number of lines in
        the file and the second element is the number of characters.
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
        return (lines, chars)


class TextAnalyzerTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self):
        """Fixture that creates a file for the text methods to use"""
        self.filename = 'text_analyzer_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('The time is now.\n'
                    'Happy new year.')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run?"""
        analyze_text(self.filename)

    def test_line_count(self):
        """Checks line count is correct"""
        self.assertEqual(analyze_text(self.filename)[0], 2)

    def test_character_count(self):
        """Checks that the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 32)

    def test_no_such_file(self):
        """Checks the proper exception is thrown for a missing file."""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Checks that the function doesn't delete the input file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()
