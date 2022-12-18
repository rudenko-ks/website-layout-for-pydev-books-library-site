import os
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def load_json(file_name: str = "books.json", folder: str = "") -> list:
    filepath = Path(folder, file_name)
    with open(filepath, 'r', encoding="utf-8") as file:
        return json.load(file)


# def get_library_pages(books_per_page: int = 10, folder: str = 'pages/'):


def on_reload():
    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template('template.html')

    books = load_json()

    books_per_page = 10
    books_on_pages = list(chunked(books, books_per_page))

    folder = 'pages/'
    Path(folder).mkdir(parents=True, exist_ok=True)

    for page_num, books_on_page in enumerate(books_on_pages, start=1):
        f_path = Path(folder, f'index{page_num}.html')
        books_page = template.render(books=books_on_page,)
        with open(f_path, 'w', encoding="utf8") as file:
            file.write(books_page)


def main():

    on_reload()

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')


if __name__ == "__main__":
    main()
