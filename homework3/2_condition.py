"""
Output numbers from 0..100 in order. First thread outputs even numbers. Second
thread outputs odd numbers.

Using Condition synchronization object.
"""

from threading import Condition
from threading import Thread


def print_even_numbers(even_printed, odd_printed):
    for i in range(0, 101, 2):
        with odd_printed:
            odd_printed.wait()
            print(i)
        with even_printed:
            even_printed.notify_all()


def print_odd_numbers(even_printed, odd_printed):
    for i in range(1, 100, 2):
        with even_printed:
            even_printed.wait()
            print(i)
        with odd_printed:
            odd_printed.notify_all()


if __name__ == '__main__':
    even_printed = Condition()
    odd_printed = Condition()

    even_thread = Thread(
        target=print_even_numbers,
        args=(even_printed, odd_printed)
    )
    odd_thread = Thread(
        target=print_odd_numbers,
        args=(even_printed, odd_printed)
    )
    even_thread.start()
    odd_thread.start()

    with odd_printed:
        odd_printed.notify_all()
