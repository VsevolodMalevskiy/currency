import csv
import random
from time import sleep

import requests
from bs4 import BeautifulSoup

import sqlite3 as sq

directory = (
    'car_id', 'data_link_to_view', 'car_brand_model_year', 'car_motor', 'car_color',
    'car_check', 'car_last_operation', 'car_wanted'
)


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


def get_detail_content(link: str) -> str:
    base_url = 'https://auto.ria.com/uk'
    url = base_url + link
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def create_car_list(car_id: str, link: str, dictionary: list) -> list:
    car_directory = (
        'car_brand_model_year', 'car_motor', 'car_color', 'car_check', 'car_last_operation', 'car_wanted'
    )

    car_inform = dict(zip(car_directory, dictionary))

    car_brand_model_year = car_inform.get('car_brand_model_year')
    car_motor = car_inform.get('car_motor')
    car_color = car_inform.get('car_color')
    car_check = car_inform.get('car_check')
    car_last_operation = car_inform.get('car_last_operation')
    car_wanted = car_inform.get('car_wanted')

    cars_data = [car_id, link, car_brand_model_year, car_motor, car_color, car_check, car_last_operation,
                 car_wanted]
    return cars_data


class CSVWriter:
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

        with open(self.filename, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)

    def write(self, row: list):
        with open(self.filename, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)


class StdOutWriter:

    def write(self, row: list):
        print(row) # noqa


class DBWriter:
    def __init__(self, db_name):
        self.db_name = db_name

        with sq.connect(self.db_name) as data_base:
            cur = data_base.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS cars(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_id INTEGER,
                data_link_to_view NVARCHAR(80),
                car_brand_model_year NVARCHAR(80),            
                car_motor NVARCHAR(40),
                car_color NVARCHAR(20),
                car_check NVARCHAR(20),
                car_last_operation INTEGER,
                car_wanted NVARCHAR(10))
            """)
            data_base.commit()

    def write(self, row: list):
        connection = sq.connect(self.db_name)
        cur = connection.cursor()
        insert_data = """INSERT INTO cars(car_id, data_link_to_view, car_brand_model_year, car_motor, 
                          car_color, car_check, car_last_operation, car_wanted)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""

        cur.execute(insert_data, row)
        connection.commit()

        cur.close()


def main():
    writers = (
        CSVWriter('cars.csv', directory),
        CSVWriter('cars2.csv', directory),
        StdOutWriter(),
        DBWriter('cars_info')
    )

    page = 2500

    while True:

        print(f'Page: {page}') # noqa

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

            main_text = get_detail_content(data_link_to_view)

            soup_detail = BeautifulSoup(main_text, features="html.parser")
            search = soup_detail.find("div", {"class": "technical-info ticket-checked"})
            try:
                search_info = search.findAll("span", {"class": "argument"})
                # search_info1 = search.findAll("span", {"class": "label"})  # наименования параметров
            except AttributeError:
                pass # noqa

            car_parameters = list()
            for item in search_info:
                car_parameters.append(item.text)

            cars_data = create_car_list(car_id, data_link_to_view, car_parameters)

            for writer in writers:
                writer.write(cars_data)

            random_sleep()


if __name__ == '__main__':
    main()
