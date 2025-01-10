import unittest

from parentnode import *
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_child(self):
        node = ParentNode(tag="p", children=[LeafNode("b", "BOLD TEXT")])
        self.assertEqual(node.to_html(), '<p><b>BOLD TEXT</b></p>')

    def test_to_html_with_multiple_children(self):
        node = ParentNode(tag="p", children=[LeafNode("b", "BOLD TEXT"), LeafNode("i", "ITALIC TEXT")])
        self.assertEqual(node.to_html(), '<p><b>BOLD TEXT</b><i>ITALIC TEXT</i></p>')

    def test_to_html_with_empty_children_list(self):
        node = ParentNode(tag="p", children=[])
        self.assertEqual(node.to_html(), '<p></p>')

    def test_to_html_with_children_of_children(self):
        node = ParentNode(tag="body", children=[ParentNode(tag="p", children=[LeafNode("b", "BOLD TEXT")])])
        self.assertEqual(node.to_html(), '<body><p><b>BOLD TEXT</b></p></body>')

    def test_raise_value_error_no_tag(self):
        node = ParentNode(tag=None, children=[])
        self.assertRaises(ValueError, node.to_html)

    def test_raise_value_error_none_children(self):
        node = ParentNode(tag="p", children=None)
        self.assertRaises(ValueError, node.to_html)



if __name__ == "__main__":
    unittest.main()