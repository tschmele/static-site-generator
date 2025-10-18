from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode

def text_node_to_html_node(node:TextNode) -> LeafNode:
    match node.text_type:
        case TextType.PLAIN:
            return LeafNode(None, node.text)
        case TextType.BOLD:
            return LeafNode("b", node.text)
        case TextType.ITALIC:
            return LeafNode("i", node.text)
        case TextType.CODE:
            return LeafNode("code", node.text)
        case TextType.LINK:
            if node.url:
                return LeafNode("a", node.text, {"href":node.url})
            raise ValueError("Missing url")
        case TextType.IMAGE:
            if node.url:
                return LeafNode("img", "", {"src":node.url, "alt":node.text})
            raise ValueError("Missing url")
        case _:
            raise ValueError("Unknown TextType")

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()

