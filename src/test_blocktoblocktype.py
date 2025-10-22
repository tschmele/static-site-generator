import unittest

from markdown_blocks import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        blocks = [
            "# heading 1",
            "## heading 2",
            "### heading 3",
            "#### heading 4",
            "##### heading 5",
            "###### heading 6"
        ]
        types = [block_to_block_type(b) for b in blocks]
        self.assertEqual(
            types,
            [
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING
            ]
        )

    def test_code(self):
        blocks = [
            "```code```",
            "```\ncode\nblock\n```"
        ]
        types = [block_to_block_type(b) for b in blocks]
        self.assertEqual(
            types,
            [
                BlockType.CODE,
                BlockType.CODE
            ]
        )

    def test_quote(self):
        blocks = [
            ">single line quote",
            ">multiline\n>quote",
            "> quote with space\n> multiline"
        ]
        types = [block_to_block_type(b) for b in blocks]
        self.assertEqual(
            types,
            [
                BlockType.QUOTE,
                BlockType.QUOTE,
                BlockType.QUOTE
            ]
        )
    
    def test_ul(self):
        blocks = [
            "- single item",
            "- multiple\n- items"
        ]
        types = [block_to_block_type(b) for b in blocks]
        self.assertEqual(
            types,
            [
                BlockType.UNORDERED_LIST,
                BlockType.UNORDERED_LIST
            ]
        )

    def test_ol(self):
        blocks = [
            "1. single item",
            "1. multiple\n2. items",
            "2. not a\n3. ordered list",
            "1. also not\n1. a ordered list"
        ]
        types = [block_to_block_type(b) for b in blocks]
        self.assertEqual(
            types,
            [
                BlockType.ORDERED_LIST,
                BlockType.ORDERED_LIST,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH
            ]
        )
