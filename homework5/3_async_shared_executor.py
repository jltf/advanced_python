"""
Use of ProcessPoolExecutor shared by coroutines.
"""
import asyncio
from concurrent.futures import ProcessPoolExecutor

N = 10 ** 2
M = 2 * 10 ** 5
TIMER_SEC = 180


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


async def sum_primes(n, m, executor, name):
    loop = asyncio.get_event_loop()
    primes_sum = 0
    for i in range(n, m):
        primes_sum += await loop.run_in_executor(executor, prime_or_zero, i)
    print('coroutine', name, 'is completed; sum is', primes_sum)
    return primes_sum


async def tick():
    for i in range(1, TIMER_SEC + 1):
        await asyncio.sleep(1)
        print(i)
    return i


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor = ProcessPoolExecutor(max_workers=2)
    results = loop.run_until_complete(
        asyncio.gather(
            sum_primes(N, M, executor, 'coroutine1'),
            sum_primes(N, M // 2, executor, 'coroutine2'),
            tick()
        )
    )
    loop.close()
    print(results)
