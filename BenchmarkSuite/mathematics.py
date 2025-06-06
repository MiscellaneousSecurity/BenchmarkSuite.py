import math, random, time

def bench_while_loop_float_sin(number_of_iterations:int=1_000_000) -> float:
    assert(isinstance(number_of_iterations, int))
    all_the_floats = [random.uniform(-1, 1) for _ in range(number_of_iterations)]
    t0 = time.perf_counter()
    iteration = 0
    while iteration < number_of_iterations:
        _ = math.sin(all_the_floats[iteration])
    t1 = time.perf_counter()
    return t1 - t0