from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from texttohtml import text_to_textnodes, text_node_to_html_node


def main():
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    print(f"{nodes=}")

if __name__ == "__main__":
    main()

