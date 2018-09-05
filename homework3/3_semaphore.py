"""
Output numbers from 0..100 in order. First thread outputs even numbers. Second
thread outputs odd numbers.

Using Semaphore synchronization object.
"""

from threading import Semaphore
from threading import Thread


def print_even_numbers(even_semaphore, odd_semaphore):
    for i in range(0, 101, 2):
        even_semaphore.acquire()
        print(i)
        odd_semaphore.release()


def print_odd_numbers(even_semaphore, odd_semaphore):
    for i in range(1, 100, 2):
        odd_semaphore.acquire()
        print(i)
        even_semaphore.release()


if __name__ == '__main__':
    even_semaphore = Semaphore(1)
    odd_semaphore = Semaphore(0)

    even_thread = Thread(
        target=print_even_numbers,
        args=(even_semaphore, odd_semaphore)
    )
    odd_thread = Thread(
        target=print_odd_numbers,
        args=(even_semaphore, odd_semaphore)
    )

    even_thread.start()
    odd_thread.start()
