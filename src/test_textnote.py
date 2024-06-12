import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.albertobenatti.com")
        node2 = TextNode("This is a text node", text_type_bold, "https://www.albertobenatti.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_image)
        self.assertEqual(repr(node), "TextNode(This is a text node, image, None)")
    
    def test_repr_with_url(self):
        node = TextNode("This is a text node", text_type_link, "https://www.albertobenatti.com")
        self.assertEqual(repr(node), f"TextNode(This is a text node, {text_type_link}, https://www.albertobenatti.com)")
    

if __name__ == "__main__":
    unittest.main()