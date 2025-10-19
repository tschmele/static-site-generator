from textnode import TextNode, TextType
import re

IMAGES = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
LINKS = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"


def extract_markdown_images(text:str) -> list[tuple[str,str]]:
    return re.findall(IMAGES, text)

def extract_markdown_links(text:str) -> list[tuple[str,str]]:
    return re.findall(LINKS, text)


def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN or not delimiter in node.text:
            new_nodes.append(node)
        elif node.text.count(delimiter) % 2 != 0:
            raise SyntaxError("Missing closing delimiter in markdown")
        else:
            index = 0
            for t in node.text.split(delimiter):
                if len(t) < 1:
                    pass
                elif delimiter in node.text[index:] and node.text[index:].index(delimiter) == 0:
                    index += len(delimiter) + len(t) + len(delimiter)
                    new_nodes.append(TextNode(t, text_type))
                else:
                    index += len(t)
                    new_nodes.append(TextNode(t, TextType.PLAIN))
            
    return new_nodes

def split_nodes_image(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            if len(images) > 0:
                i = 0
                for img in images:
                    md = f"![{img[0]}]({img[1]})"
                    if len(node.text[i:i+node.text[i:].index(md)]) > 0:
                        new_nodes.append(TextNode(node.text[i:i+node.text[i:].index(md)], TextType.PLAIN))
                        i += node.text[i:].index(md)
                    new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
                    i += len(md)
                if len(node.text[i:]) > 0:
                    new_nodes.append(TextNode(node.text[i:], TextType.PLAIN))
            else:
                new_nodes.append(node)

    return new_nodes

def split_nodes_link(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if len(links) > 0:
                i = 0
                for link in links:
                    md = f"[{link[0]}]({link[1]})"
                    if len(node.text[i:i+node.text[i:].index(md)]) > 0:
                        new_nodes.append(TextNode(node.text[i:i+node.text[i:].index(md)], TextType.PLAIN))
                        i += node.text[i:].index(md)
                    new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                    i += len(md)
                if len(node.text[i:]) > 0:
                    new_nodes.append(TextNode(node.text[i:], TextType.PLAIN))
            else:
                new_nodes.append(node)

    return new_nodes