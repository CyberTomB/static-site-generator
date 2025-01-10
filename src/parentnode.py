from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props, value=None)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode has no tag")
        elif self.children == None:
            raise ValueError("ParentNode has no children!")
        children_output = ''
        for c in self.children:
            children_output += c.to_html()
        return f"<{self.tag}>{children_output}</{self.tag}>"