"""
Output numbers from 0..100 in order. First thread outputs even numbers. Second
thread outputs odd numbers.

Using Timer synchronization object.
"""

from threading import Timer
import time

TIME_INTERVAL = 0.01


def print_even_numbers():
    for i in range(0, 101, 2):
        print(i)
        time.sleep(TIME_INTERVAL)


def print_odd_numbers():
    for i in range(1, 100, 2):
        print(i)
        time.sleep(TIME_INTERVAL)


if __name__ == '__main__':
    even_timer = Timer(0, print_even_numbers)
    odd_timer = Timer(TIME_INTERVAL / 2, print_odd_numbers)

    even_timer.start()
    odd_timer.start()
