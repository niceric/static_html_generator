class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props 

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        attributes = []    
        for k, v in self.props.items():
            attributes.append(f' {k.strip('"')}="{v}"')
        return "".join(attributes)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" 
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value = None, props=None):
        super().__init__(tag, value, None, props)
        self.tag = tag 
        self.value = value
        self.props = props 

        if self.value is None:
            raise ValueError("Value is required")

    def to_html(self):    

            
        if self.tag is None:
            return self.value
 
        return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'
    



class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props=None):
        super().__init__(tag, None, children, props)
        self.children = children
        self.tag = tag
        self.props = props 

        if self.children == None or self.children == []:
            raise ValueError("Children is required")
        
        if self.tag == None:
            raise ValueError("Tag is required")
        
    def to_html(self):    
        string_of_children = ""

        for child in self.children:
            string_of_children += child.to_html()

        return f'<{self.tag}>{string_of_children}</{self.tag}>'     
 


        