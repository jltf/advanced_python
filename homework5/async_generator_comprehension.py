"""
Use of ProcessPoolExecutor shared by coroutines.
"""
import asyncio
from concurrent.futures import ProcessPoolExecutor

N = 10 ** 2 // 5
M = 10 ** 5 // 5
TIMER_SEC = 10


def check_prime(n):
    """Checks is n is prime number"""
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(3, n, 2):
        if n % m == 0:
            return False
    return True


async def asum(async_gen):
    s = 0
    async for i in async_gen:
        s += i
    return s


async def sum_primes(n, m, executor, name):
    loop = asyncio.get_event_loop()
    primes_sum = await asum(
        num * await loop.run_in_executor(executor, check_prime, num)
        for num in range(n, m)
    )
    print('coroutine', name, 'is completed; sum is', primes_sum)
    return primes_sum


async def timer(sec):
    for i in range(1, sec + 1):
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
            timer(TIMER_SEC)
        )
    )
    loop.close()
    print(results)
