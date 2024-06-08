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

            if len(links) == 0:
                  new_nodes.append(node)
                  continue
            for link in links:
                  sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
                  if len(sections) != 2:
                        raise ValueError("Invalid markdown, link section not closed.")
                  if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], text_type_text))
                  new_nodes.append(
                        TextNode(
                              link[0],
                              text_type_link,
                              link[1]
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



node_2 = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )
new_nodes = split_nodes_link([node_2])

def text_to_textnodes(text):
      nodes = [TextNode(text, text_type_text)]
      nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
      nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
      nodes = split_nodes_delimiter(nodes, "`", text_type_code)
      nodes = split_nodes_image(nodes)
      nodes = split_nodes_link(nodes)
      return nodes 


text_document = 'This is **bolded** paragraph \n\nThis is another paragraph with *italic* text and `code` here \nThis is the same paragraph on a new line \n\n* This is a list \n* with items'

def markdown_to_blocks(markdown): 
      block_list = []
      splitted_text = markdown.split("\n\n")
      for split in splitted_text:
            block_list.append(split.replace("\n", ""))
      return block_list

print(markdown_to_blocks(text_document))







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

