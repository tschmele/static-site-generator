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

def generate_pages_recursive(src_dir_path:str, template_path:str, dest_dir_path:str):
    for file in os.listdir(src_dir_path):
        src = join(src_dir_path, file)
        dst = join(dest_dir_path, file)
        if isfile(src) and ".md" in file:
            generate_page(src, template_path, dst[:-3]+".html")
        else:
            os.mkdir(dst)
            generate_pages_recursive(src, template_path, dst)
