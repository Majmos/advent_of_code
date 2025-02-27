import time


def measure_time(func):
    def wrapper():
        start_time: float = time.time()

        func()

        end_time: float = time.time()
        print(
            f"execution time: {(end_time - start_time) * 1000 :.4f} milliseconds")
    return wrapper
