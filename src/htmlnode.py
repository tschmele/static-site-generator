

class HTMLNode():
    def __init__(self, tag:str|None=None, value:str|None=None, children:list[HTMLNode]|None=None, props:dict[str,str]|None=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            html = []
            for p in self.props:
                html.append(f'{p}="{self.props[p]}"')
            return " ".join(html)
        return None

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Missing value")
        if not self.tag:
            return self.value
        match self.tag:
            case 'a':
                return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
            case 'img':
                return f"<{self.tag} {self.props_to_html()} />"
            case _:
                return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag")
        if not self.children or len(self.children) < 1:
            raise ValueError("Missing children")
        return f'<{self.tag}>{"".join([c.to_html() for c in self.children])}</{self.tag}>'
