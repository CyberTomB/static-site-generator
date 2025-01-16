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
        result = split_nodes_delimiter([node], TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], TextNode)
        self.assertEqual(result[0].text, "This will have a ")
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " markdown.")

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This will have an *italic* markdown.", "text")
        result = split_nodes_delimiter([node], TextType.ITALIC)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], TextNode)
        self.assertEqual(result[0].text, "This will have an ")
        self.assertEqual(result[1].text, "italic")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text, " markdown.")

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This will have a `code` markdown.", "text")
        result = split_nodes_delimiter([node], TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], TextNode)
        self.assertEqual(result[0].text, "This will have a ")
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " markdown.")

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This will have a `code` markdown.", "text")
        result = split_nodes_delimiter([node], TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], TextNode)
        self.assertEqual(result[0].text, "This will have a ")
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " markdown.")

    def test_split_nodes_delimiter_missing_closing_tag_raises_error(self):
        node = TextNode("This is missing a terminal *demarcation bottom text", "text")
        with self.assertRaises(Exception) as cm:
            split_nodes_delimiter([node], TextType.ITALIC)
        exception = cm.exception
        self.assertEqual(Exception, exception.__class__)
        self.assertTrue("Missing terminal demarcation" in str(exception))

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        # Expecting: [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
        # ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        output = extract_markdown_images(text)
        self.assertEqual(len(output), 2)
        self.assertEqual(output[0][0], "rick roll")
        self.assertEqual(output[0][1], "https://i.imgur.com/aKaOqIh.gif")
        self.assertEqual(output[1][0], "obi wan")
        self.assertEqual(output[1][1], "https://i.imgur.com/fJRm4Vk.jpeg")
        

if __name__ == "__main__":
    unittest.main()