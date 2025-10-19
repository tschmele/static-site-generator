import unittest

from textnode import TextNode, TextType
from main import text_to_textnodes


class TestTextToNodes(unittest.TestCase):
    def test_all_at_once(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is ", TextType.PLAIN, None), 
                TextNode("text", TextType.BOLD, None), 
                TextNode(" with an ", TextType.PLAIN, None), 
                TextNode("italic", TextType.ITALIC, None), 
                TextNode(" word and a ", TextType.PLAIN, None), 
                TextNode("code block", TextType.CODE, None), 
                TextNode(" and an ", TextType.PLAIN, None), 
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), 
                TextNode(" and a ", TextType.PLAIN, None), 
                TextNode("link", TextType.LINK, "https://boot.dev")
            ]
        )