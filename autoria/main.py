import csv
import random
from time import sleep

import requests
from bs4 import BeautifulSoup


def random_sleep():
    sleep(random.randint(1, 5))


def get_page_content(page: int, size: int = 100) -> str:
    query_parameters = {
        'indexName': 'auto,order_auto,newauto_search',
        'country.import.usa.not': '-1',
        'price.currency': '1',
        'abroad.not': '-1',
        'custom.not': '-1',
        'page': page,
        'size': size
    }
    base_url = 'https://auto.ria.com/uk/search/'
    response = requests.get(base_url, params=query_parameters)
    response.raise_for_status()
    return response.text


class CSVWriter:
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

        with open(self.filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)

    def write(self, row: list):
        with open(self.filename, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)


class StdOutWriter:

    def write(self, row: list):
        print(row)


def main():
    writers = (
        CSVWriter('cars.csv', ['car_id', 'data_link_to_view']),
        CSVWriter('cars2.csv', ['car_id', 'data_link_to_view']),
        # StdOutWriter()
    )

    page = 1500

    while True:

        print(f'Page: {page}')

        page_content = get_page_content(page)

        page += 1

        soup = BeautifulSoup(page_content, features="html.parser")

        search_results = soup.find("div", {"id": "searchResults"})
        ticket_items = search_results.find_all("section", {"class": "ticket-item"})

        if not ticket_items:
            break

        for ticket_item in ticket_items:
            car_details = ticket_item.find("div", {"class": "hide"})
            car_id = car_details['data-id']
            data_link_to_view = car_details['data-link-to-view']

            for writer in writers:
                writer.write([car_id, data_link_to_view])

        random_sleep()


if __name__ == '__main__':
    main()
