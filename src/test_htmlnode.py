import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        node = HtmlNode("p", "inside value", [], {"href": "https://www.google.com"})
        self.assertEqual(node.__repr__(), f"HtmlNode({node.tag}, {node.value}, {node.children}, {node.props})")

    def test_no_props(self):
        node = HtmlNode("p")
        self.assertEqual(node.props, None)

    def test_no_props_to_html_is_empty_string(self):
        node = HtmlNode("p")
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html(self):
        node = HtmlNode(props={
            'href': 'https://www.boot.dev',
            'target': '_blank'
        })

        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')
if __name__ == "__main__":
    unittest.main()