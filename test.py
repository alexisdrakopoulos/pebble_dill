from pebble_dill import ProcessPool


def add(x):
    return x + 5


if __name__ == "__main__":

    futures = []
    with ProcessPool(max_workers=3) as pool:
        for i in range(9):
            futures.append(pool.schedule(add, kwargs={"x": i}))

    print([future.result() for future in futures])
