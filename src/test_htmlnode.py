import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_blank(self):
        node = HTMLNode()
        text = f"HTMLNode(None, None, None, None)"
        self.assertEqual(str(node),text)

    def test_tag(self):
        node = HTMLNode("a")
        text = f"HTMLNode(a, None, None, None)"
        self.assertEqual(str(node),text)

    def test_value(self):
        node = HTMLNode("a", "boot.dev")
        text = f"HTMLNode(a, boot.dev, None, None)"
        self.assertEqual(str(node),text)

    def test_children(self):
        node = HTMLNode("a", "boot.dev", [HTMLNode()])
        text = f"HTMLNode(a, boot.dev, [HTMLNode(None, None, None, None)], None)"
        self.assertEqual(str(node),text)

    def test_props(self):
        node = HTMLNode("a", "boot.dev", [HTMLNode()], {"href":"https://www.boot.dev"})
        text = f"HTMLNode(a, boot.dev, [HTMLNode(None, None, None, None)], href=https://www.boot.dev)"
        self.assertEqual(str(node),text)

    def test_tohtmlerr(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()