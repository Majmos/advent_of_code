import time


def measure_time(func):
    def wrapper():
        start_time: float = time.perf_counter()

        func()

        end_time: float = time.perf_counter()
        print(
            f"execution time: {(end_time - start_time) * 1000 :.4f} milliseconds")
    return wrapper
