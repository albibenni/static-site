import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        child1 = HTMLNode("p", "some text", [], {"href": "https://www.google.com", "target": "_blank"})
        child2 = HTMLNode("p", "some text", [child1], {"href": "https://www.google.com", "target": "_blank"})
        node = HTMLNode("p", "some text", [child1, child2], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(repr(node), f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})")

    def test_props_to_html(self):
        child1 = HTMLNode("p", "some text", [], {"href": "https://www.google.com", "target": "_blank"})
        child2 = HTMLNode("p", "some text", [child1], {"href": "https://www.google.com", "target": "_blank"})
        node = HTMLNode("p", "some text", [child1, child2], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"') 
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_parentNod(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_to_html_parentNode_without_children(self):
        node = ParentNode(
            "p",
            [
            ],
            )
        self.assertEqual(node.to_html(), "<p></p>")
    
    def test_to_html_parentNode_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )
        with self.assertRaises(ValueError):
            node.to_html()