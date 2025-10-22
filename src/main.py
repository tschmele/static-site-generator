from generate_page import generate_pages_recursive
from copyfiles import clean_directory, copy_files


def main():
    clean_directory("public/")
    copy_files("static/", "public/")
    generate_pages_recursive("content/", "template.html", "public/")

if __name__ == "__main__":
    main()

