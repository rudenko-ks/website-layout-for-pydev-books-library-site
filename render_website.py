import os
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def get_book_descriptions_from_file(file_name: str = "books.json", folder: str = "library/") -> list:
    filepath = Path(folder, file_name)
    with open(filepath, 'r', encoding="utf-8") as file:
        return json.load(file)


def on_reload():
    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template('/templates/template.html')

    books = get_book_descriptions_from_file()

    books_per_page = 16
    books_on_pages = list(chunked(books, books_per_page))
    max_pages = len(books_on_pages)

    folder = 'pages/'
    Path(folder).mkdir(parents=True, exist_ok=True)

    for page_num, books_on_page in enumerate(books_on_pages, start=1):
        f_path = Path(folder, f'index{page_num}.html')
        books_page = template.render(
            books=books_on_page,
            max_pages=max_pages,
            current_page=page_num,
        )
        with open(f_path, 'w', encoding="utf8") as file:
            file.write(books_page)


def main():

    on_reload()

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.', default_filename='pages/index1.html')


if __name__ == "__main__":
    main()
