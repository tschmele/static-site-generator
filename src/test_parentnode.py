import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_list(self):
        child1 = LeafNode("li", "item 1")
        child2 = LeafNode("li", "item 2")
        child3 = LeafNode("li", "item 3")
        parent = ParentNode("ul", [child1, child2, child3])
        self.assertEqual(
            parent.to_html(),
            "<ul><li>item 1</li><li>item 2</li><li>item 3</li></ul>"
        )

    def test_to_html_valueerror(self):
        parent = ParentNode("div", [])
        with self.assertRaisesRegex(ValueError, "Missing children"):
            parent.to_html()

