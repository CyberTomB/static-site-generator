import unittest

from conversions import *

class TestConversions(unittest.TestCase):
    def test_text_to_html_plain_text(self):
        text = "Plain text here"
        text_node = TextNode(text, "text")
        node = text_node_to_html_node(text_node)
        self.assertEqual(text, node.to_html())
        self.assertIsInstance(node, LeafNode)

    def test_bold_to_html(self):
        text = "This will be bold"
        text_node = TextNode(text, "bold")
        node = text_node_to_html_node(text_node)
        self.assertEqual(f"<b>{text}</b>", node.to_html())
        self.assertIsInstance(node, LeafNode)
        self.assertIsInstance(node, LeafNode)

    def test_italic_to_html(self):
        text = "This will be italic"
        text_node = TextNode(text, "italic")
        node = text_node_to_html_node(text_node)
        self.assertEqual(f"<i>{text}</i>", node.to_html())
        self.assertIsInstance(node, LeafNode)

    def test_code_to_html(self):
        text = "This will be code"
        text_node = TextNode(text, "code")
        node = text_node_to_html_node(text_node)
        self.assertEqual(f"<code>{text}</code>", node.to_html())
        self.assertIsInstance(node, LeafNode)

    def test_link_to_html(self):
        text = "This will be link"
        text_node = TextNode(text, "link", url="www.url.com")
        node = text_node_to_html_node(text_node)
        self.assertEqual(f"<a href=\"www.url.com\">{text}</a>", node.to_html())
        self.assertIsInstance(node, LeafNode)

    def test_image_to_html(self):
        text = "This will be image"
        text_node = TextNode(text, "image", url="www.url.com")
        node = text_node_to_html_node(text_node)
        self.assertEqual(f"<img src=\"www.url.com\" alt=\"{text}\"></img>", node.to_html())
        self.assertIsInstance(node, LeafNode)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This will have a **bold** markdown.", "text")
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], TextNode)
        self.assertEqual(result[0].text, "This will have a ")
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " markdown.")


if __name__ == "__main__":
    unittest.main()