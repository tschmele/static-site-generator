import unittest

from markdown_blocks import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_single_title(self):
        md = "# header 1"
        self.assertEqual(
            extract_title(md),
            "header 1"
        )
    
    def test_multiple_titles(self):
        md = "# header 1\n## header 2"
        self.assertEqual(
            extract_title(md),
            "header 1"
        )

    def test_title_in_middle(self):
        md = "leading paragraph\n## header 2\n# header 1\nclosing paragraph"
        self.assertEqual(
            extract_title(md),
            "header 1"
        )

    def test_no_title(self):
        md = "## header 2"
        with self.assertRaisesRegex(
            ValueError,
            "markdown contains no title"
        ):
            extract_title(md)
