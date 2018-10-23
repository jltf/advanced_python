# Currency converging package

Small package dedicated to currency convertion and multi-currency operations.

Class which representing money in different currencies. It supports
the following operations:

>>> x = Money(10, 'BYN')
>>> y = Money(11)  # define your own default value, e.g. USD
>>> z = Money(12.34, 'EUR')
>>> print(z +  3.11 * x + y * 0.8) # result in EUR, two digits after point
543.21 EUR

>>> lst = [Money(10, 'BYN'), Money(11), Money(12.01, 'JPY')]
>>> s = sum(lst)
>>> print(s)  # result in BYN
123.45 BYN
