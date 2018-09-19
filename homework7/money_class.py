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


def get_rate(currency, target_currency):
    try:
        byn_rates = get_rate.byn_rates
    except AttributeError:
        json_data = urllib.request.urlopen(RATES_URL).read()
        rates = json.loads(json_data)
        byn_rates = {'BYN': 1}
        for rate in rates:
            byn_rates[rate['Cur_Abbreviation']] = (
                float(rate['Cur_OfficialRate']) * int(rate['Cur_Scale'])
            )
        get_rate.byn_rates = byn_rates
    conversion_rate = (
        byn_rates[currency.name] / byn_rates[target_currency.name]
    )
    return conversion_rate


class Money:
    def __init__(self, value, currency=Currency.USD):
        self.value = value
        self.currency = currency

    def __str__(self):
        return '{} {}'.format(self.value, self.currency)

    def __repr__(self):
        return '<{}({}, {})>'.format(
            self.__class__.__name__, self.value, self.currency
        )

    def __add__(self, other):
        other_value = other.value * get_rate(other.currency, self.currency)
        return Money(self.value + other_value, self.currency)

    def __radd__(self, other):
        return Money(self.value + other, self.currency)

    def __mul__(self, other):
        return Money(self.value * other, self.currency)

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == '__main__':
    x = Money(10, Currency.BYN)
    y = Money(11)
    z = Money(12.34, Currency.EUR)

    print(z + 3.11 * x + y * 0.8)

    print(sum([x, y, z]))
