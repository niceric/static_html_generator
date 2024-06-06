import re 


# for testing 
text_images = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
text_html = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    splitted = matches
    return matches

def extract_markdown_html(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    splitted = matches
    return matches




#print(extract_markdown_images(text_images))
#print(extract_markdown_html(text_html))



