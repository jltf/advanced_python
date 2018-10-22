import asyncio
from concurrent.futures import ProcessPoolExecutor

N = 10 ** 2
M = 2 * 10 ** 5


def prime_or_zero(n):
    """returns n if it is prime number, otherwise returns 0"""
    if n < 2:
        return 0
    if n == 2:
        return 2
    for m in range(2, n):
        if n % m == 0:
            return 0
    return n


async def sum_primes(n, m):
    loop = asyncio.get_event_loop()
    executor = ProcessPoolExecutor()

    tasks = [loop.run_in_executor(executor, prime_or_zero, i)
             for i in range(n, m)]

    completed, pending = await asyncio.wait(tasks)

    return sum(t.result() for t in completed)


if __name__ == '__main__':
    print(asyncio.run(sum_primes(N, M)))
