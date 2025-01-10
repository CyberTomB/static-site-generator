from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if(self.value == None):
            raise ValueError()
        if(not self.tag == None):
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            return f'{self.value}'
