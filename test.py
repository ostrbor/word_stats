from unittest import TestCase
from unittest.mock import patch, MagicMock
from collections import OrderedDict
from process import count_words, sort_statistics


class TestProcess(TestCase):
    def setUp(self):
        self.lines = ['a b', 'b c c c']

    def test_count_words(self):
        mock_fd_content = MagicMock()
        mock_fd = MagicMock()

        expected = {'a': 1, 'b': 2, 'c': 3}
        with patch('process.open') as mock_open:
            mock_fd.__enter__.return_value = mock_fd_content
            mock_fd_content.__iter__.return_value = iter(self.lines)
            mock_open.return_value = mock_fd

            actual = count_words('/path/to/file')
            self.assertDictEqual(expected, actual)

    def test_sort_statistics(self):
        data = {'aa': 1, 'ab': 1, 'c': 2}
        expected = OrderedDict([('c', 2), ('aa', 1), ('ab', 1)])
        actual = sort_statistics(data)
        self.assertDictEqual(expected, actual)
