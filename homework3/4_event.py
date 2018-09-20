"""
Output numbers from 0..100 in order. First thread outputs even numbers. Second
thread outputs odd numbers.

Using Event synchronization object.
"""

from threading import Event
from threading import Thread


def print_even_numbers(even_printed, odd_printed):
    for i in range(0, 101, 2):
        odd_printed.wait()
        odd_printed.clear()
        print(i)
        even_printed.set()


def print_odd_numbers(even_printed, odd_printed):
    for i in range(1, 100, 2):
        even_printed.wait()
        even_printed.clear()
        print(i)
        odd_printed.set()


if __name__ == '__main__':
    even_printed = Event()
    odd_printed = Event()

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
    odd_printed.set()
