import os
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server

def load_json(file_name: str = "books.json", folder: str = "") -> list:
    filepath = Path(folder, file_name)
    with open(filepath, 'r', encoding="utf-8") as file:
        return json.load(file)


def on_reload():
    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template('template.html')

    books = load_json()

    books_page = template.render(
        books=books,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(books_page)


def main():

    on_reload()

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')

if __name__ == "__main__":
    main()
