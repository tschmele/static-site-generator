from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link


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
        
def text_to_textnodes(text:str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.PLAIN)]
    delimiters = {
        "`": TextType.CODE,
        "**": TextType.BOLD,
        "_": TextType.ITALIC
    }
    for d in delimiters:
        nodes = split_nodes_delimiter(nodes, d, delimiters[d])
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def main():
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    print(f"{nodes=}")

if __name__ == "__main__":
    main()

