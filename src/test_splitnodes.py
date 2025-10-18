import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def test_single_split_middle(self):
        node = TextNode("This has a **bold** word", TextType.PLAIN)
        splits = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            splits,
            [
                TextNode("This has a ", TextType.PLAIN),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.PLAIN)
            ]
        )

    def test_single_split_start(self):
        node = TextNode("**This** has a bold word", TextType.PLAIN)
        splits = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            splits,
            [
                TextNode("This", TextType.BOLD),
                TextNode(" has a bold word", TextType.PLAIN)
            ]
        )
        
    def test_single_split_end(self):
        node = TextNode("This has a **bold word**", TextType.PLAIN)
        splits = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            splits,
            [
                TextNode("This has a ", TextType.PLAIN),
                TextNode("bold word", TextType.BOLD)
            ]
        )

    def test_single_split_multiple(self):
        node = TextNode("**This** has a **bold word**", TextType.PLAIN)
        splits = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            splits,
            [
                TextNode("This", TextType.BOLD),
                TextNode(" has a ", TextType.PLAIN),
                TextNode("bold word", TextType.BOLD)
            ]
        )
    
    def test_multiple_split_plain(self):
        nodes = [
            TextNode("This has a **bold** word", TextType.PLAIN),
            TextNode("**This** has a bold word", TextType.PLAIN),
            TextNode("This has a **bold word**", TextType.PLAIN),
            TextNode("**This** has a **bold word**", TextType.PLAIN)
        ]
        splits = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(
            splits,
            [
                TextNode("This has a ", TextType.PLAIN),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.PLAIN),
                TextNode("This", TextType.BOLD),
                TextNode(" has a bold word", TextType.PLAIN),
                TextNode("This has a ", TextType.PLAIN),
                TextNode("bold word", TextType.BOLD),
                TextNode("This", TextType.BOLD),
                TextNode(" has a ", TextType.PLAIN),
                TextNode("bold word", TextType.BOLD)
            ]
        )

    def test_multiple_split_mixed(self):
        nodes = [
            TextNode("This has a **bold** word", TextType.PLAIN),
            TextNode("**This** has a bold word", TextType.PLAIN),
            TextNode("This has a ", TextType.PLAIN),
            TextNode("bold word", TextType.BOLD),
            TextNode("**This** has a **bold word**", TextType.PLAIN)
        ]
        splits = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(
            splits,
            [
                TextNode("This has a ", TextType.PLAIN),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.PLAIN),
                TextNode("This", TextType.BOLD),
                TextNode(" has a bold word", TextType.PLAIN),
                TextNode("This has a ", TextType.PLAIN),
                TextNode("bold word", TextType.BOLD),
                TextNode("This", TextType.BOLD),
                TextNode(" has a ", TextType.PLAIN),
                TextNode("bold word", TextType.BOLD)
            ]
        )

    def test_split_code(self):
        node = TextNode("This has a `code` block", TextType.PLAIN)
        splits = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            splits,
            [
                TextNode("This has a ", TextType.PLAIN),
                TextNode("code", TextType.CODE),
                TextNode(" block", TextType.PLAIN)
            ]
        )

    def test_split_italic(self):
        node = TextNode("This has an _italic_ word", TextType.PLAIN)
        splits = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            splits,
            [
                TextNode("This has an ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.PLAIN)
            ]
        )
