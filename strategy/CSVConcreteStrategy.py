import csv
from typing import List

from strategy.Strategy import Strategy


class CSVConcreteStrategy(Strategy):
    def do(self, data: List):
        with open('resources/data.csv', 'w', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['ID', 'POSITION', 'COMPANY', 'NET', "TECH", "CITY", 'LINK'])
            for item in data:
                writer.writerow([item.index, item.position, item.company, item.fork, item.tech, item.loc, item.link])