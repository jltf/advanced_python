"""
Output numbers from 0..100 in order. First thread outputs even numbers. Second
thread outputs odd numbers.

Using Lock synchronization object.
"""

from threading import Lock
from threading import Thread


def print_even_numbers(lock_even, lock_odd):
    for i in range(0, 101, 2):
        lock_odd.acquire()
        print(i)
        lock_even.release()


def print_odd_numbers(lock_even, lock_odd):
    for i in range(1, 100, 2):
        lock_even.acquire()
        print(i)
        lock_odd.release()


if __name__ == '__main__':
    lock_even = Lock()
    lock_even.acquire()
    lock_odd = Lock()

    even_thread = Thread(
        target=print_even_numbers,
        args=(lock_even, lock_odd)
    )
    odd_thread = Thread(
        target=print_odd_numbers,
        args=(lock_even, lock_odd)
    )

    even_thread.start()
    odd_thread.start()
