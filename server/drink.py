from collections import defaultdict
from pprint import pprint
import json


class Drink:
    def __init__(self):
        self.category = defaultdict(set)
        for drink, cat in self.load("./resources/db/category.csv"):
            self.category[cat].add(drink)

        self.drink = defaultdict(list)
        for place, name, price in self.load("./resources/db/place.csv"):
            self.drink[name].append([int(price), place])

    @staticmethod
    def load(path):
        with open(path, "r") as f:
            for i, line in enumerate(f):
                if not i:
                    continue
                yield line.replace("\n", "").split(",")

    def get_category(self, category):
        dic = {"nods": 0, "drinks": {}}
        for drink in self.category[category]:
            d = defaultdict(dict)
            min_price = (drinks := sorted(self.drink[drink]))[0][0]
            for price, place in drinks:
                if price != min_price:
                    break
                d[drink].update({place: price})
            dic["drinks"].update(d)
            dic["nods"] += 1
        pprint(dic)
        return json.dumps(dic, ensure_ascii=False)


if __name__ == '__main__':
    dr = Drink()
    dr.get_category("清涼飲料水")
