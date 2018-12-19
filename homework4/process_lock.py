import multiprocessing as mp


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
    lock_even = mp.Lock()
    lock_even.acquire()
    lock_odd = mp.Lock()

    even_process = mp.Process(
        target=print_even_numbers,
        args=(lock_even, lock_odd)
    )
    odd_process = mp.Process(
        target=print_odd_numbers,
        args=(lock_even, lock_odd)
    )

    even_process.start()
    odd_process.start()
