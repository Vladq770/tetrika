import csv

import requests

from bs4 import BeautifulSoup


def get_beasts_count_by_char(base_url: str, start_page: str) -> dict[str, int]:
    """
    Получить словарь с количеством животных на каждую букву алфавита.

    Args:
        base_url: Базовый url адрес.
        start_page: Адрес начальной страницы.

    Returns:
        Словарь с количеством животных.
    """
    beast_count = {}
    process_category_page(base_url, start_page, beast_count)
    return beast_count


def process_category_page(base_url: str, url: str, beast_count: dict[str, int]) -> None:
    """
    Получить словарь с количеством животных на каждую букву алфавита.

    Args:
        base_url: Базовый url адрес.
        url: Адрес конкретной страницы.
        beast_count: Словарь с количеством животных.
    """
    response = requests.get(base_url + url)
    soup = BeautifulSoup(response.text, "html.parser")
    beasts = soup.select("#mw-pages > div.mw-content-ltr > div")[0].select("li a")

    for beast in beasts:
        first_char = beast["title"][0].upper()
        # Вики после кириллицы переходит на латиницу, если латиница не нужна, следует прекратить парсинг.
        if first_char == "A":
            return
        beast_count[first_char] = beast_count.get(first_char, 0) + 1

    next_page = soup.find("a", string="Следующая страница")
    if next_page:
        next_url = next_page["href"]
        process_category_page(base_url, next_url, beast_count)


def write_csv(data: dict, file_name: str = "beasts"):
    """
    Записать данные в csv файл.

    Args:
        data: Данные для записи.
        file_name: Имя файла.
    """
    with open(f"{file_name}.csv", "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # writer.writerow(['Буква', 'Количество'])

        for letter, value in sorted(data.items()):
            writer.writerow([letter, value])


if __name__ == "__main__":
    base_url = "https://ru.wikipedia.org"
    start_page = "/wiki/Категория:Животные_по_алфавиту"
    beast_count = get_beasts_count_by_char(base_url, start_page)
    write_csv(beast_count, "beasts")
