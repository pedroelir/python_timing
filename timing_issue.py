import sys
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
    t0: int = time.perf_counter_ns()
    timeout: float = sleep_time * 1000_000_000
    while (time.perf_counter_ns() - t0 < timeout):
        pass



get_time_clock = "perf_counter"
get_time_ns = time.perf_counter_ns
sleep = custom_sleep
# sleep = time.sleep

def loop_func(func, args, loops):
    # measurements =[]
    # for _ in range(loops):
    #     measurement = measure_time(func=func, args=args)
    #     measurements.append(measurement)
    # return measurements

    return[measure_time(func=func,args=args) for _ in range(loops)]

def loop_func_with_break(func, args, loops):
    # measurements =[]
    # for _ in range(loops):
    #     sleep(1)
    #     measurement = measure_time(func=func, args=args)
    #     measurements.append(measurement)
    # return measurements
    def measure_time_with_brake(func, args):
        sleep(1)
        return measure_time(func=func,args=args)
    return[measure_time_with_brake(func=func,args=args) for _ in range(loops)]

def main_print():
    loops = 10
    product_dot_args = (1,)
    print(f"clock info for {get_time_clock}")
    print(time.get_clock_info(get_time_clock))
    print(sys.version_info)

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
    product_args = (10,)
    global sleep
    # print("First call product_times_10")
    initial_call = measure_time(product_times_10,product_args)
    call_without_break = loop_func(product_times_10, product_args,loops=10)
    sleep = lambda x:x**x
    call_with_break_lambda = loop_func_with_break(product_times_10, product_args,loops=10)
    sleep = custom_sleep
    call_with_break_custom_sleep = loop_func_with_break(product_times_10, product_args,loops=10)
    sleep = print
    call_with_break_print = loop_func_with_break(product_times_10, product_args,loops=10)
    sleep = time.sleep
    call_with_break_time_sleep = loop_func_with_break(product_times_10, product_args,loops=10)
    print(f"{initial_call=},")
    print(f"{call_without_break=},")
    print(f"{call_with_break_lambda=}.")
    print(f"{call_with_break_custom_sleep=}.")
    print(f"{call_with_break_print=}.")
    print(f"{call_with_break_time_sleep=}.")


if __name__ == "__main__":
    # main_print()
    main_time()
