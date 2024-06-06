from htmlnode import LeafNode

# create variables for each text_type to be used in the text to html function
# why = easier to edit 
#
#
#
#
#
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
        def __init__(self, text, text_type, url = None):
            self.text = text
            self.text_type = text_type
            self.url = url
        def __eq__(self, other):
              return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        def __repr__(self):
              return f"TextNode({self.text}, {self.text_type}, {self.url})"
            
def text_node_to_html_node(text_node):
      if text_node.text_type == "text":
            return LeafNode(None, text_node.text, None)
      if text_node.text_type == "bold":
            return LeafNode("b", text_node.text, None)
      if text_node.text_type == "italic":
            return LeafNode("i", text_node.text, None)
      if text_node.text_type == "code":
            LeafNode("code", text_node.text, None)
      if text_node.text_type == "link":
            LeafNode("a", text_node.text, {"href": text_node.url})
      if text_node.text_type == "image":
            LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
      else:
            raise Exception("Wrong text type")
      
def split_nodes_delimiter(old_nodes, delimiter, text_type):
      print(delimiter)
      new_nodes = []      
      if old_nodes == None:
            raise ValueError("The old_nodes list cannot be empty")
      for old_node in old_nodes:
            if old_node.text_type is not text_type_text:
                  new_nodes.append(old_node)
                  continue
            split_nodes = []
            splitted_text = old_node.text.split(delimiter)
            if len(splitted_text) % 2 == 0:
                  raise ValueError("Invalid markdown, formatted section not closed")
            for i in range(len(splitted_text)):

                  if splitted_text[i] == "":
                        continue
                  if i % 2 == 0:
                        split_nodes.append(TextNode(splitted_text[i], text_type_text))
                  else:
                        split_nodes.append(TextNode(splitted_text[i], text_type))
            new_nodes.extend(split_nodes)
      return new_nodes            
        

node = TextNode("This is text with a `code block` word", text_type_text)
node2 = TextNode("This is not text_type", text_type_image, "www.google.com")
node3 = TextNode("This is **bold** text", text_type_text)
node4 = TextNode("This is another string with **some bold text**", text_type_text)


new_nodes = split_nodes_delimiter([node, node2, node3, node4], "**", text_type_bold)
print(new_nodes)
new_nodes2 = split_nodes_delimiter([node, node2, node3, node4], "`", text_type_code)
print(new_nodes2)
