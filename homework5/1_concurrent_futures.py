"""
Homework 5.

Output sum of prime numbers in the specified range [n, m).
Using concurrent.futures.

"""
from concurrent.futures import ProcessPoolExecutor

N = 10 ** 2
M = 2 * 10 ** 5


def prime_or_zero(n):
    """returns n if it is prime number, otherwise returns 0"""
    if n < 2:
        return 0
    if n == 2:
        return n
    for m in range(3, n, 2):
        if n % m == 0:
            return 0
    return n


if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        print(sum(executor.map(prime_or_zero, range(N, M))))
