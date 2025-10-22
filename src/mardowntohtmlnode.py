from enum import Enum

from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from textnode import TextNode,TextType
from texttohtml import text_node_to_html_node, text_to_textnodes


class HTMLTag(Enum):
    HEADING = "h"
    PARAGRAPH = "p"
    UNORDERED_LIST = "ul"
    ODERED_LIST = "ol"
    LIST_ITEM = "li"
    BLOCKQUOTE = "blockquote"
    CODE = "code"
    DIV = "div"
    SPAN = "span"
    PRE = "pre"


def text_to_list_items(block):
    lines = block.split("\n")
    text_nodes = [text_to_textnodes(line[2:].strip()) for line in lines]
    list_items = []
    for tn in text_nodes:
        list_items.append(ParentNode(HTMLTag.LIST_ITEM.value, [text_node_to_html_node(node) for node in tn]))
    return list_items

def markdown_to_html_node(markdown:str) -> HTMLNode:
    html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type = block_to_block_type(block)
        match type:
            case BlockType.HEADING:
                splits = block.split(" ", 1)
                tag = f"{HTMLTag.HEADING.value}{splits[0].count("#")}"
                text_nodes = text_to_textnodes(splits[1])
                children = [text_node_to_html_node(tn) for tn in text_nodes]
                html_nodes.append(ParentNode(tag, children))
            case BlockType.PARAGRAPH:
                tag = HTMLTag.PARAGRAPH.value
                text_nodes = text_to_textnodes(block.replace("\n", " "))
                children = [text_node_to_html_node(tn) for tn in text_nodes]
                html_nodes.append(ParentNode(tag, children))
            case BlockType.CODE:
                tag = HTMLTag.CODE.value
                content = text_node_to_html_node(TextNode(block[4:-3],TextType.PLAIN))
                html_nodes.append(ParentNode(HTMLTag.PRE.value, [ParentNode(tag, [content])]))
            case BlockType.QUOTE:
                tag = HTMLTag.BLOCKQUOTE.value
                clean = "\n".join([line[1:].strip() for line in block.split("\n")])
                text_nodes = text_to_textnodes(clean)
                children = [text_node_to_html_node(tn) for tn in text_nodes]
                html_nodes.append(ParentNode(tag, children))
            case BlockType.UNORDERED_LIST:
                tag = HTMLTag.UNORDERED_LIST.value
                html_nodes.append(ParentNode(tag, text_to_list_items(block)))
            case BlockType.ORDERED_LIST:
                tag = HTMLTag.ODERED_LIST.value
                html_nodes.append(ParentNode(tag, text_to_list_items(block)))
            case _:
                raise TypeError("unknown block_type")
    
    return ParentNode(HTMLTag.DIV.value, html_nodes)