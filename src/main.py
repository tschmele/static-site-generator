from generate_page import generate_page
from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from texttohtml import text_to_textnodes, text_node_to_html_node

from copyfiles import clean_directory, copy_files


def main():
    clean_directory("public/")
    copy_files("static/", "public/")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()

