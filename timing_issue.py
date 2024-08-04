import sys
import time
import random


def calculate_dot_product(size) -> int:
    vector1: list[int] = [random.randint(0, 100) for _ in range(size)]
    vector2: list[int] = [random.randint(0, 100) for _ in range(size)]
    return sum([i * j for (i, j) in zip(vector1, vector2)])


def product_times_10(num) -> int:
    return 10 * num


def custom_sleep(sleep_time: float) -> None:
    t0: int = time.perf_counter_ns()
    timeout: float = sleep_time * 1000_000_000
    while time.perf_counter_ns() - t0 < timeout:
        pass


GET_TIME_CLOCK = "perf_counter"
get_time_ns = time.perf_counter_ns
sleep = custom_sleep
# sleep = time.sleep


def measure_time(func, args) -> int:
    t0 = get_time_ns()
    func(*args)
    return get_time_ns() - t0


def measure_time_with_brake(func, args):
    sleep(0.01)
    return measure_time(func=func, args=args)


def loop_func(func, args, loops):
    return [measure_time(func=func, args=args) for _ in range(loops)]


def loop_func_with_break(func, args, loops):

    return [measure_time_with_brake(func=func, args=args) for _ in range(loops)]


def print_py_info():
    print(f"clock info for {GET_TIME_CLOCK}")
    print(time.get_clock_info(GET_TIME_CLOCK))
    print(sys.version_info)


def main_print():
    loops = 10
    product_dot_args = (1,)
    print_py_info()

    # print("First call calculate_dot_product")
    # print(measure_time(calculate_dot_product, product_dot_args))
    # print(f"Call calculate_dot_product {loops} times without a break")
    # for _ in range(loops):
    #     print(measure_time(calculate_dot_product, product_dot_args))
    # print(f"Call calculate_dot_product {loops} times without a 1 second break")
    # for _ in range(loops):
    #     sleep(1)
    #     print(measure_time(calculate_dot_product, product_dot_args))

    print("First call product_times_10")
    print(measure_time(product_times_10, product_dot_args))
    print(f"Call product_times_10 {loops} times without a break")
    for _ in range(loops):
        print(measure_time(product_times_10, product_dot_args))
    print(f"Call product_times_10 {loops} times without a 1 second break")
    for _ in range(loops):
        sleep(1)
        print(measure_time(product_times_10, product_dot_args))


def main_time():
    global sleep
    test_func = product_times_10
    test_args = (10,)
    loops = 25
    # print("First call product_times_10")
    initial_call = measure_time(test_func, test_args)
    call_without_break = loop_func(test_func, test_args, loops=loops)
    sleep = lambda x: x**x
    call_with_break_lambda = loop_func_with_break(test_func, test_args, loops=loops)
    sleep = custom_sleep
    call_with_break_custom_sleep = loop_func_with_break(test_func, test_args, loops=loops)
    sleep = print
    call_with_break_print = loop_func_with_break(test_func, test_args, loops=loops)
    sleep = time.sleep
    call_with_break_time_sleep = loop_func_with_break(test_func, test_args, loops=loops)
    print_py_info()
    print(f"{initial_call=},")
    print(f"{call_without_break=},")
    print(f"{call_with_break_lambda=}.")
    print(f"{call_with_break_custom_sleep=}.")
    print(f"{call_with_break_print=}.")
    print(f"{call_with_break_time_sleep=}.")


if __name__ == "__main__":
    main_time()
