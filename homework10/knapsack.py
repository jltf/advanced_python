from contextlib import suppress
import csv
from functools import total_ordering

CAPACITY = 400  # weight in dag


@total_ordering
class Item(object):
    def __init__(self, title, weight, value):
        self.title = title
        self.weight = weight
        self.value = value
        self.efficiency = self.value / self.weight

    def __repr__(self):
        return f'<Item({self.title}, {self.weight}, {self.value})>'

    def __str__(self):
        return f'{self.title}({self.weight}, {self.value})'

    def __eq__(self, other):
        return self.efficiency == other.efficiency

    def __lt__(self, other):
        return self.efficiency < other.efficiency


class DoesNotFit(Exception):
    pass


class Pack(object):
    def __init__(self, capacity):
        self.weight = 0
        self.items = list()
        self.capacity = capacity

    def add(self, item):
        if not self.will_fit(item):
            raise DoesNotFit

        self.items.append(item)
        self.weight += item.weight

    def will_fit(self, item):
        if self.weight + item.weight > self.capacity:
            return False
        return True

    def __str__(self):
        item_string = ', '.join(str(i) for i in self.items)
        return f'[{item_string}]\nTotal weight: {self.weight}'

if __name__ == '__main__':
    def iter_items(filename):
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                title = row['item']
                weight = int(row['weight(dag)'])
                value = int(row['value'])
                yield Item(title, weight, value)

    pack = Pack(capacity=CAPACITY)

    with suppress(DoesNotFit):
        for item in sorted(iter_items('items.csv'), reverse=True):
            pack.add(item)

    print(pack)
