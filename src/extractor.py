import re 


# for testing 
text_images = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
text_html = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
text_images_2 = "This is text with an IMAGE and (KORVAR.GOOGLE.COM/IMAGE.PNG)"


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_html(text):
    pattern_html = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern_html, text)
    return matches




print(extract_markdown_images(text_images))
print(extract_markdown_html(text_html))
print(extract_markdown_images(text_images_2))


