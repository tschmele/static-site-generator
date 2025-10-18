import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_notag(self):
        node = LeafNode(None, "no tag")
        self.assertEqual(node.to_html(), "no tag")

    def test_p(self):
        node = LeafNode("p", "paragraph")
        self.assertEqual(node.to_html(), "<p>paragraph</p>")

    def test_a(self):
        node = LeafNode("a", "link to boot.dev", {"href":"https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">link to boot.dev</a>')

    def test_img(self):
        node = LeafNode("img", "this is an image", {"src":"some.link", "alt":"alt text"})
        self.assertEqual(node.to_html(), '<img src="some.link" alt="alt text" />')
    