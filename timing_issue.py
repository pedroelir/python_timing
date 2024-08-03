import time
import random


def calculate_dot_product(size) -> int:
    vector1: list[int] = [random.randint(0, 100) for _ in range(size)]
    vector2: list[int] = [random.randint(0, 100) for _ in range(size)]
    return sum([i * j for (i, j) in zip(vector1, vector2)])

def product_times_10(num) -> int:
    return 10*num


def measure_time(func, args) -> int:
    t0 = get_time_ns()
    func(*args)
    return get_time_ns() - t0

def custom_sleep(sleep_time:float) -> None:
    t0: int = time.process_time_ns()
    timeout: float = sleep_time * 1000_000_000
    while (time.process_time_ns() - t0 < timeout):
        pass



get_time_clock = "perf_counter"
get_time_ns = time.perf_counter_ns
sleep = custom_sleep


def main():
    loops = 10
    product_dot_args = (1,)
    print(f"clock info for {get_time_clock}")
    print(time.get_clock_info(get_time_clock))
    print("First call calculate_dot_product")
    print(measure_time(calculate_dot_product, product_dot_args))
    print(f"Call calculate_dot_product {loops} times without a break")
    for _ in range(loops):
        print(measure_time(calculate_dot_product, product_dot_args))
    print(f"Call calculate_dot_product {loops} times without a 1 second break")
    for _ in range(loops):
        print(measure_time(calculate_dot_product, product_dot_args))
        sleep(1)

    print("First call product_times_10")
    print(measure_time(product_times_10, product_dot_args))
    print(f"Call product_times_10 {loops} times without a break")
    for _ in range(loops):
        print(measure_time(product_times_10, product_dot_args))
    print(f"Call product_times_10 {loops} times without a 1 second break")
    for _ in range(loops):
        print(measure_time(product_times_10, product_dot_args))
        sleep(1)


if __name__ == "__main__":
    main()
