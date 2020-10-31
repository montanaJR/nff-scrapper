import json
from typing import List

from strategy.Strategy import Strategy


class JSONConcreteStrategy(Strategy):
    def do(self, data: List):
        with open('resources/data.json', 'w', encoding="utf-8") as json_file:
            for item in data:
                json.dump(item.to_dict(), json_file)
