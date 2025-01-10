from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode):
    value, type = text_node.text, text_node.text_type

    match type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=value)
        case TextType.BOLD:
            return LeafNode(tag="b", value=value)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=value)
        case TextType.CODE:
            return LeafNode(tag="code", value=value)
        case TextType.LINK:
            return LeafNode(tag="a", value=value, props={
                "href": text_node.url
            })
        case TextType.IMAGE:
            return LeafNode(tag="img", value='', props={
                "src": text_node.url,
                "alt": value
            })
        case _:
            return value
    