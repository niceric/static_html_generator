import unittest 

from textnode import TextNode
from htmlnode import LeafNode, HTMLNode, ParentNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text, None)
    if text_node.text_type == "bold":
        return LeafNode("b", text_node.text, None)
    if text_node.text_type == "italic":
        return LeafNode("i", text_node.text, None)
    if text_node.text_type == "code":
        return LeafNode("code", text_node.text, None)
    if text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == "image":
        return LeafNode("img", "", {"src": text_node.url})
    else:
        raise Exception("Wrong text type")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes == None:
        raise ValueError("The old_nodes list cannot be empty")
    new_list_of_nodes = []

    for node in old_nodes:
        if node.text_type != text_type:
            new_list_of_nodes.append(node)
            continue
        list_of_splitted = []
        if delimiter in node.text:
            list_of_splitted = node.text.split(delimiter)
            for splitted_part in list_of_splitted:
                new_list_of_nodes.append(TextNode(f"{splitted_part}", text_type_bold, None))
        else:
            raise Exception("Delimiter not valid, invalid markdown syntax")
    print(new_list_of_nodes)        
                
                
        #new_node = 
                
                
              #  print(list_of_splitted)
            #the_text = node.text
            
            #print(the_text)
            #node.text.split("**") 

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a **text** node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node_text_type = TextNode("This is a text node", "flat", None)
        node_text_type2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node_text_type, node_text_type2)
    def test_eq(self):
        node = None #TextNode(None, None, None)
        node2 = None #TextNode(None, None, None)
        self.assertIsNone(node, node2)


    
    def test_text_to_html(self):
        node_text_type = TextNode("This is a text node", "bold", None)
        html_node = text_node_to_html_node(node_text_type)
        result = html_node.to_html()
        print(result)

    def test_split_nodes_delimiter(self):
        node1 = TextNode("This is a **bold** node", "bold", None)
        print(split_nodes_delimiter([node1], "**", "bold"))


if __name__ == "__main__":
    unittest.main()

