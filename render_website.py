import os
import json
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

def load_json(file_name: str = "books.json", folder: str = "") -> list:
    filepath = Path(folder, file_name)
    with open(filepath, 'r', encoding="utf-8") as file:
        return json.load(file)


def main():
    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template('template.html')

    books = load_json()

    books_page = template.render(
        books=books,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(books_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
