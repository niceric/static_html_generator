import unittest 

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a value", [], {"href": "https://www.google.com"})
        node = HTMLNode("p", "This is a value", [], {"href": "https://www.google.com"})
        self.assertEqual(node, node)
    
    def test_not_eq(self):
        node = HTMLNode("p", "This is a value", [None], {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "This is a value", [None], {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)
    
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a value", None, {
            "href": "https://www.google.com", 
            "target": "_blank"
            })
        result = node.props_to_html()
        expected_output = ' href="https://www.google.com" target="_blank"'
    
        self.assertEqual(result, expected_output)
        #"href": "https://www.google.com"



    def test_html_to(self):
        node_leaf_1 = LeafNode("a", "This is value TEXT", {"href": "https://www.leafnode-tohtml.com"})
        #node2 = LeafNode(None, "This is value TEXT", {"href": "https://www.google.com"})
        result_node1 = node_leaf_1.to_html()
        self.assertEqual(result_node1, '<a href="https://www.leafnode-tohtml.com">This is value TEXT</a>')

    def test_no_tag(self):
        node_no_tag = LeafNode(value="Value string", props={"href": "https://www.leafnode-tohtml.com"})
        result_no_tag = node_no_tag.to_html()
        self.assertEqual(result_no_tag, "Value string")


    def test_parent(self):
        node = ParentNode(
                    tag ="p", children=
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )

        result = node.to_html()
        print(result)

if __name__ == "__main__":
    unittest.main()

