import sys
from generate_page import generate_pages_recursive
from copyfiles import clean_directory, copy_files


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    clean_directory("docs/")
    copy_files("static/", "docs/")
    generate_pages_recursive("content/", "template.html", "docs/", basepath)

if __name__ == "__main__":
    main()

