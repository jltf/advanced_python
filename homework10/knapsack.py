"""
A tourist wants to make a good trip at the weekend with his friends.
They will go to the mountains to see the wonders of nature, so he
needs to pack well for the trip.

He has a good knapsack for carrying things, but knows that he can
carry a maximum of only 4kg in it, and it will have to last the
whole day. He creates a list of what he wants to bring for the trip
but the total weight of all items is too much. He then decides to add
columns to his initial list detailing their weights and a numerical
value representing how important the item is for the trip. The tourist
can choose to take any combination of items from the list, but only one
of each item is available. He may not cut or diminish the items, so he
can only take whole units of any item.
"""


from collections import namedtuple
from itertools import takewhile
from functools import total_ordering
import csv

CAPACITY = 400  # weight in dag


@total_ordering
class Item:
    def __init__(self, title, weight, value):
        self.title = title
        self.weight = weight
        self.value = value
        self.efficiency = self.value / self.weight

    def __repr__(self):
        return f'Item({self.title}, {self.weight}, {self.value})'

    def __str__(self):
        return self.__repr__

    def __eq__(self, other):
        return self.efficiency == other.efficiency

    def __lt__(self, other):
        return self.efficiency < other.efficiency

class Pack:
    def __init__(self):
        self.weight = 0
        self.items = list()

    def add(self, item):
        if not self.will_fit(item):
            raise ValueError

        self.items.append(item)
        self.weight += item.weight

    def will_fit(self, item):
        if self.weight + item.weight > CAPACITY:
            return False
        return True

    def __str__(self):
        return str(self.items) + str(self.weight)



if __name__ == '__main__':
    def iter_items(filename):
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                weight = int(row['weight(dag)'])
                value = int(row['value'])
                yield Item(row['item'], weight, value)

    pack = Pack()

    try:
        for item in sorted(iter_items('items.csv'), reverse=True):
            pack.add(item)
    except ValueError:
        pass

    print(pack)
