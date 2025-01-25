from textnode import TextNode, TextType
from leafnode import LeafNode
from enum import Enum
from re import findall

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


class DelimiterType(Enum):
    BOLD = "**"
    ITALIC = "*"
    CODE = "`"

def split_nodes_delimiter(old_nodes: list[TextNode], text_type):
    final_nodes = []
    for node in old_nodes:
        new_nodes = []
        split_text = node.text.split(DelimiterType[TextType(text_type).name].value)
        if(not len(split_text) % 3 == 0):
            raise Exception("Missing terminal demarcation")
        for i in range(len(split_text)):
            if not i % 2 == 0:
                new_nodes.append(TextNode(split_text[i], text_type=text_type))
            else:
                new_nodes.append(TextNode(split_text[i], text_type="text"))
        final_nodes.extend(new_nodes)
    print(f">>>split: {final_nodes}")
    return final_nodes

def split_nodes_image(old_nodes: list[TextNode]):
    pass

def split_nodes_link(old_nodes: list[TextNode]):
    final_nodes = []
    for node in old_nodes:
        current_text = node.text
        links = extract_markdown_links(node.text)
        for text, url in links:
            splits = current_text.split(f"[{text}]({url})", 1)
            final_nodes.append(TextNode(splits[0], TextType.TEXT))
            current_text = splits[1]
            final_nodes.append(TextNode(text, TextType.LINK, url))

    return final_nodes

def extract_markdown_images(text):
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return findall(regex, text)

def extract_markdown_links(text):
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return findall(regex, text)