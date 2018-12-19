"""
Homework 7.

Create class representing money in different currencies. It has to
support the following operations:

>>> x = Money(10, 'BYN')
>>> y = Money(11)  # define your own default value, e.g. USD
>>> z = Money(12.34, 'EUR')
>>> print(z +  3.11 * x + y * 0.8) # result in EUR, two digits after point
543.21 EUR

>>> lst = [Money(10, 'BYN'), Money(11), Money(12.01, 'JPY')]
>>> s = sum(lst)
>>> print(s)  # result in BYN
123.45 BYN

(Optional): Get the latest exchange rates from any free API.
For example, https://currencylayer.com/

"""

import enum
import json
import urllib.request

RATES_URL = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'


@enum.unique
class Currency(enum.Enum):
    EUR = 978
    USD = 840
    BYN = 933

    def __str__(self):
        return self.name


class Money(object):
    byn_rates = None

    def __init__(self, value, currency=Currency.USD):
        self.value = value
        self.currency = currency

    def __str__(self):
        return f'{self.value:.2f} {self.currency}'

    def __repr__(self):
        return f'<{self.__class__.name}({self.value}, {self.currency})>'

    def __add__(self, other):
        converted = other.convert(self.currency)
        return Money(self.value + converted.value, self.currency)

    def __radd__(self, other):
        return Money(self.value + other, self.currency)

    def __mul__(self, other):
        return Money(self.value * other, self.currency)

    def __rmul__(self, other):
        return self.__mul__(other)

    @staticmethod
    def fetch_byn_rates():
        byn_rates = Money.byn_rates
        if byn_rates:
            return byn_rates
        json_data = urllib.request.urlopen(RATES_URL).read()
        rates = json.loads(json_data)
        byn_rates = {'BYN': 1}
        for rate in rates:
            byn_rates[rate['Cur_Abbreviation']] = (
                float(rate['Cur_OfficialRate']) * int(rate['Cur_Scale'])
            )
        Money.byn_rates = byn_rates
        return byn_rates

    @staticmethod
    def get_rate(currency, target_currency):
        byn_rates = Money.fetch_byn_rates()
        conversion_rate = (
            byn_rates[currency.name] / byn_rates[target_currency.name]
        )
        return conversion_rate

    def convert(self, target_currency):
        value = (
            self.value * self.get_rate(self.currency, target_currency)
        )
        return Money(value, target_currency)


if __name__ == '__main__':
    x = Money(10, Currency.BYN)
    y = Money(11)
    z = Money(12.34, Currency.EUR)

    print(z + 3.11 * x + y * 0.8)

    print(sum([x, y, z]))
