import unittest

from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_to_html_without_props(self):
        node = LeafNode("p", "This is the inner value")
        self.assertEqual(node.to_html(), "<p>This is the inner value</p>")

    def test_to_html_with_props(self):
        node = LeafNode("p", "This is the inner value", {"href":"https://www.boot.dev", "target":"_blank"})
        self.assertEqual(node.to_html(), '<p href="https://www.boot.dev" target="_blank">This is the inner value</p>')

    def test_no_value(self):
        node = LeafNode(tag=None, value=None)
        self.assertRaises(ValueError, node.to_html)

    def test_no_tag(self):
        node = LeafNode(value="There is a value", tag=None)
        self.assertEqual(node.value, node.to_html())


if __name__ == "__main__":
    unittest.main()