import argparse
import os
import json
from pathlib import Path
import sys

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def create_argparser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='''\
        Скрипт представляет собой пример создания библиотеки научно-фантастических книг.
        В карточках книг на странице будут собраны данные в виде заголовков, автора,
        текста книг в формате .txt и обложек страниц при их наличии.''',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '--filepath',
        help='Путь к JSON-файлу с данными о книгах. По умолчанию: library/books.json',
        type=str,
        default='library/books.json')
    return parser.parse_args()


def get_book_descriptions_from_file(filepath: str) -> list:
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def on_reload():
    args = create_argparser()

    if not Path(args.filepath).is_file():
        print('Указанный файл не найден.')
        sys.exit(0)

    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template('/templates/template.html')

    books = get_book_descriptions_from_file(args.filepath)

    book_cards_per_page = 16
    book_cards_on_pages = list(chunked(books, book_cards_per_page))
    max_pages = len(book_cards_on_pages)

    folder = 'pages/'
    Path(folder).mkdir(parents=True, exist_ok=True)

    for page_num, books_on_page in enumerate(book_cards_on_pages, start=1):
        f_path = Path(folder, f'index{page_num}.html')
        books_page = template.render(
            books=books_on_page,
            max_pages=max_pages,
            current_page=page_num,
        )
        with open(f_path, 'w', encoding='utf8') as file:
            file.write(books_page)


def main():

    on_reload()

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.', default_filename='pages/index1.html')


if __name__ == '__main__':
    main()
