import os
from os.path import exists, join, isfile

from mardowntohtmlnode import markdown_to_html_node
from markdown_blocks import extract_title

def generate_page(src_path:str, template_path:str, dest_path:str):
    print(f"generating page from {src_path} to {dest_path} using {template_path}")

    with open(src_path) as f:
        markdown = f.read()
    
    with open(template_path) as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    content = html_node.to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    if not exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    
    with open(dest_path, "w") as f:
        f.write(template)