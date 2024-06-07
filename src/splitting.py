from textnode import text_node_to_html_node, text_type_bold, text_type_code, text_type_image, text_type_italic, text_type_link, text_type_text, TextNode
from extractor import extract_markdown_html, extract_markdown_images

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
            elif node.text == "":
                  raise ValueError("Input text needed.")      
            elif extract_markdown_images(node.text) == []:
                  raise ValueError("The markdown needs to contain a link to an image.")
            split_nodes = []
            extracted_text = extract_markdown_images(node.text)

            # if len(extracted_text) % 2 == 0:
            #       raise ValueError("Invalid markdown, formatted section not closed")
            for i in range(len(extracted_text)):

                  if extracted_text[i] == "":
                        continue
                  if i % 2 == 0:
                        split_nodes.append(TextNode(extracted_text[i], text_type_image))
            new_nodes.extend(split_nodes)
      return new_nodes    
            
            


node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
)
new_nodes = split_nodes_image([node])



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

