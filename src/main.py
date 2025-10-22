from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from texttohtml import text_to_textnodes, text_node_to_html_node

from copyfiles import copy_static_files


def main():
    copy_static_files("static/", "public/")

if __name__ == "__main__":
    main()

