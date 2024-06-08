import re
from textnode import text_node_to_html_node, text_type_bold, text_type_code, text_type_image, text_type_italic, text_type_link, text_type_text, TextNode


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_html(text):
    pattern_html = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern_html, text)
    return matches



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
        

def split_nodes_image(old_nodes):
      new_nodes = []
      if old_nodes == None:
            raise ValueError("The list cannot be empty")
      for node in old_nodes:
            if node.text_type is not text_type_text:
                  new_nodes.append(node)
                  continue                
            
            original_text = node.text
            images = extract_markdown_images(original_text)

            if len(images) == 0:
                  new_nodes.append(node)
                  continue
            for image in images: 
                  sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
                  if len(sections) != 2:
                        raise ValueError("Invalid markdown, image section not closed.")
                  if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], text_type_text))
                  new_nodes.append(
                        TextNode(
                              image[0],
                              text_type_image,
                              image[1]
                        )
                  )
                  original_text = sections[1]
            if original_text != "":
                  new_nodes.append(TextNode(original_text, text_type_text))
      
      return new_nodes    
            
def split_nodes_link(old_nodes):
      new_nodes = []
      if old_nodes == None:
            raise ValueError("The list cannot be empty")
      for node in old_nodes:
            if node.text_type is not text_type_text:
                  new_nodes.append(node)
                  continue                
            
            original_text = node.text
            links = extract_markdown_html(original_text)

            if len(html) == 0:
                  new_nodes.append(node)
                  continue
            for block in html: 
                  sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
                  if len(sections) != 2:
                        raise ValueError("Invalid markdown, image section not closed.")
                  if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], text_type_text))
                  new_nodes.append(
                        TextNode(
                              image[0],
                              text_type_image,
                              image[1]
                        )
                  )
                  original_text = sections[1]
            if original_text != "":
                  new_nodes.append(TextNode(original_text, text_type_text))
      
      return new_nodes    
            
            



















node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
)
new_nodes = split_nodes_image([node])
print(new_nodes)













# node = TextNode("This is text with a `code block` word", text_type_text)
# node2 = TextNode("This is not text_type", text_type_image, "www.google.com")
# node3 = TextNode("This is **bold** text", text_type_text)
# node4 = TextNode("This is another string with **some bold text**", text_type_text)


# new_nodes = split_nodes_delimiter([node, node2, node3, node4], "**", text_type_bold)
# print(new_nodes)
# new_nodes2 = split_nodes_delimiter([node, node2, node3, node4], "`", text_type_code)
# print(new_nodes2)


# node_image = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#                       text_type_text
# )

