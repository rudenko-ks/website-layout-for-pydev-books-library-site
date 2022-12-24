# Верстаем онлайн библиотеку

В [предыдущем проекте](https://github.com/rudenko-ks/website-layout-for-pydev-books-library) мы научились парсить данные онлайн библиотеки [tululu.org](tululu.org)
по страницам и по категориям.

Скрипт представляет собой пример создания библиотеки научно-фантастических книг. В карточках книг на странице будут собраны данные в виде заголовков, автора, текста книг в формате `.txt` и обложек страниц при их наличии.

## Пример карточек книг на странице
![Скриншот страницы сайта](https://github.com/rudenko-ks/website-layout-for-pydev-books-library-site/blob/main/static/screenshot.png)

## Пример работы сайта
Посмотреть пример работы сайта можно на [GitHub Pages](https://rudenko-ks.github.io/website-layout-for-pydev-books-library-site/pages/index1.html)

## Установка и запуск

Python3 должен быть уже установлен. 
1. Клонируйте репозиторий
```shell
https://github.com/rudenko-ks/website-layout-for-pydev-books-library-site.git
```
2. Создайте виртуальное окружение
```shell
python -m venv .venv
source .venv/bin/activate
```
3. Используйте `pip` (или `pip3`, если конфликт с Python2) для установки зависимостей
```shell
pip install -r requirements.txt
```
4. Запустите сайт командой 
```shell
python render_website.py
``` 
Скрипт генерирует страницы сайта в каталоге `pages` и запустит библиотеку на локальном сервере по адресу `127.0.0.1:5500/pages/index1.html`  

Не запуская скрипт библиотеку книг можно посмотреть открыв файл `<DOWNLOADED_PROJECT_FOLDER>/pages/index1.html`. Сайт откроется в веб-браузере.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).


> Written with [StackEdit](https://stackedit.io/).
