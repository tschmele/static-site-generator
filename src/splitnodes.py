from textnode import TextNode, TextType


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
