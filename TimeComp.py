if __name__ == '__main__':
    from timeit import timeit
    import random

    data = random.sample(range(-1000, 1000), 1000)

    print(timeit(
        f"((Solution()).maximumProduct({data}))",
        number=100000,
        setup="from __main__ import Solution"
    ))